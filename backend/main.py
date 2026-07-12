from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
from utils.config import settings
from utils.seed_knowledge import ensure_default_files
from database import init_db

app = FastAPI(
    title="AI Sports Equipment Recognition and Recommendation System",
    description="FastAPI backend for CNN equipment detection, FAISS RAG search, and Gemini AI recommendations.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin, "http://localhost:3000", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ensure_default_files()
init_db()
app.include_router(router)

@app.get("/")
def root():
    return {
        "message": "AI Sports Equipment Assistant backend is running",
        "docs": "/docs",
        "health": "/health",
    }

@app.get("/health")
def health():
    return {"status": "ok", "service": settings.app_name}
