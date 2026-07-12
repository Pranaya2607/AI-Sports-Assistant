import json
from typing import Dict, List

from utils.config import settings

class RagPipeline:
    def __init__(self):
        self.vector_dir = settings.resolved_vector_db_dir
        self.index_path = self.vector_dir / "sports_equipment.index"
        self.chunks_path = self.vector_dir / "sports_equipment_chunks.json"
        self._index = None
        self._chunks = None

    def _load(self):
        if self._chunks is not None:
            return
        if not self.index_path.exists() or not self.chunks_path.exists():
            from rag.build_vector_db import build_vector_db
            build_vector_db()
        import faiss
        import google.generativeai as genai
        genai.configure(api_key=settings.gemini_api_key)
        self._index = faiss.read_index(str(self.index_path))
        self._chunks = json.loads(self.chunks_path.read_text(encoding="utf-8"))

    def search(self, query: str, top_k: int = 4) -> List[Dict]:
        try:
            self._load()
            import numpy as np
            import google.generativeai as genai
            
            resp = genai.embed_content(model="models/gemini-embedding-2", content=query)
            query_embedding = np.asarray([resp["embedding"]], dtype="float32")
            norms = np.linalg.norm(query_embedding, axis=1, keepdims=True)
            query_embedding = query_embedding / norms
            
            scores, indices = self._index.search(query_embedding, top_k)
            results = []
            for score, idx in zip(scores[0], indices[0]):
                if idx < 0:
                    continue
                item = self._chunks[int(idx)]
                results.append({
                    "score": round(float(score), 4),
                    "source": item["source"],
                    "text": item["text"],
                })
            return results
        except Exception as exc:
            return self.keyword_fallback(query, top_k=top_k, error=str(exc))

    def keyword_fallback(self, query: str, top_k: int = 4, error: str | None = None) -> List[Dict]:
        kb_dir = settings.resolved_knowledge_base_dir
        query_terms = set(query.lower().split())
        results = []
        for path in kb_dir.rglob("*"):
            if path.is_file() and path.suffix.lower() in {".md", ".txt"}:
                text = path.read_text(encoding="utf-8", errors="ignore")
                paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
                for paragraph in paragraphs:
                    words = set(paragraph.lower().split())
                    score = len(query_terms & words)
                    if score > 0:
                        results.append({"score": float(score), "source": path.name, "text": paragraph[:1200]})
        results = sorted(results, key=lambda x: x["score"], reverse=True)[:top_k]
        if not results and error:
            results.append({"score": 0.0, "source": "system", "text": f"RAG search fallback activated because vector search failed: {error}"})
        return results

rag_pipeline = RagPipeline()
