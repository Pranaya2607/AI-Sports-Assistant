# Installation Guide

## Prerequisites

- Python 3.10 or above
- Node.js 18 or above
- npm
- A Google Gemini API key
- A sports equipment image dataset arranged into train, valid, and test folders

## Backend Installation

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r ../requirements.txt
cp .env.example .env
```

Edit `.env` and add:

```env
GEMINI_API_KEY=your_actual_key
```

Build the vector database:

```bash
python rag/build_vector_db.py
```

Start backend:

```bash
uvicorn main:app --reload --port 8000
```

## Frontend Installation

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`.
