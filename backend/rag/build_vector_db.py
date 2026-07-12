import json
from pathlib import Path
import sys

import faiss
import numpy as np
import google.generativeai as genai

CURRENT_DIR = Path(__file__).resolve().parent
BACKEND_DIR = CURRENT_DIR.parent
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from rag.text_processing import chunk_text, load_documents
from utils.config import settings
from utils.seed_knowledge import ensure_default_files


def build_vector_db() -> dict:
    ensure_default_files()
    kb_dir = settings.resolved_knowledge_base_dir
    vector_dir = settings.resolved_vector_db_dir
    vector_dir.mkdir(parents=True, exist_ok=True)

    if not settings.gemini_api_key:
        raise ValueError("GEMINI_API_KEY is not set in .env. Required for Gemini Embeddings.")
    
    genai.configure(api_key=settings.gemini_api_key)

    records = []
    for source, text in load_documents(kb_dir):
        for idx, chunk in enumerate(chunk_text(text)):
            records.append({"source": source, "chunk_id": idx, "text": chunk})

    if not records:
        raise RuntimeError(f"No documents found in knowledge base: {kb_dir}")

    print(f"Generating embeddings for {len(records)} chunks using Gemini...")
    embed_vectors = []
    for r in records:
        resp = genai.embed_content(model="models/gemini-embedding-2", content=r["text"])
        embed_vectors.append(resp["embedding"])

    embeddings = np.asarray(embed_vectors, dtype="float32")
    # Gemini embeddings aren't perfectly normalized by default, so we normalize them for inner-product
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    embeddings = embeddings / norms
    
    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, str(vector_dir / "sports_equipment.index"))
    (vector_dir / "sports_equipment_chunks.json").write_text(json.dumps(records, indent=2), encoding="utf-8")

    return {"chunks": len(records), "vector_db_dir": str(vector_dir)}


if __name__ == "__main__":
    print(json.dumps(build_vector_db(), indent=2))
