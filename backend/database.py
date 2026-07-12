import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from utils.config import settings

DB_PATH = Path(__file__).resolve().parent / settings.database_path

@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()

def init_db() -> None:
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS prediction_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            equipment TEXT,
            confidence REAL,
            status TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        conn.execute("""
        CREATE TABLE IF NOT EXISTS ai_query_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            equipment TEXT,
            question TEXT,
            answer TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

def log_prediction(equipment: str | None, confidence: float, status: str) -> None:
    init_db()
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO prediction_history (equipment, confidence, status) VALUES (?, ?, ?)",
            (equipment, confidence, status),
        )

def log_ai_query(equipment: str | None, question: str, answer: str) -> None:
    init_db()
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO ai_query_history (equipment, question, answer) VALUES (?, ?, ?)",
            (equipment, question, answer),
        )
