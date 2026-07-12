from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[1]
PROJECT_ROOT = BASE_DIR.parent

class Settings(BaseSettings):
    app_name: str = "AI Sports Equipment Assistant"
    app_env: str = "development"
    frontend_origin: str = "http://localhost:5173"
    gemini_api_key: str = ""
    gemini_model: str = "gemini-2.5-flash"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    model_path: str = "cnn/sports_model.pth"
    classes_path: str = "cnn/classes.json"
    knowledge_base_dir: str = "../knowledge_base"
    vector_db_dir: str = "vector_db"
    database_path: str = "app.db"

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", env_file_encoding="utf-8", extra="ignore")

    @property
    def resolved_model_path(self) -> Path:
        return (BASE_DIR / self.model_path).resolve()

    @property
    def resolved_classes_path(self) -> Path:
        return (BASE_DIR / self.classes_path).resolve()

    @property
    def resolved_knowledge_base_dir(self) -> Path:
        return (BASE_DIR / self.knowledge_base_dir).resolve()

    @property
    def resolved_vector_db_dir(self) -> Path:
        return (BASE_DIR / self.vector_db_dir).resolve()

settings = Settings()
