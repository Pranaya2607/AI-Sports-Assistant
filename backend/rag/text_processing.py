from pathlib import Path
from typing import List, Tuple

from pypdf import PdfReader


def read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def read_pdf(path: Path) -> str:
    reader = PdfReader(str(path))
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n".join(pages)


def load_documents(kb_dir: Path) -> List[Tuple[str, str]]:
    documents = []
    for path in kb_dir.rglob("*"):
        if path.is_dir():
            continue
        suffix = path.suffix.lower()
        if suffix in {".md", ".txt"}:
            documents.append((path.name, read_text_file(path)))
        elif suffix == ".pdf":
            documents.append((path.name, read_pdf(path)))
    return documents


def chunk_text(text: str, chunk_size: int = 800, overlap: int = 160) -> List[str]:
    text = " ".join(text.split())
    if not text:
        return []
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end == len(text):
            break
        start = max(0, end - overlap)
    return chunks
