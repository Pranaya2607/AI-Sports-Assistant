# Backend

FastAPI backend for the AI Sports Equipment Assistant.

## Run

```bash
pip install -r ../requirements.txt
uvicorn main:app --reload --port 8000
```

## Train CNN

```bash
python cnn/train.py --data-dir ../dataset --epochs 15 --batch-size 16
```

## Build RAG DB

```bash
python rag/build_vector_db.py
```
