# Testing Guide

## Backend Manual Testing

Run backend:

```bash
cd backend
uvicorn main:app --reload --port 8000
```

Open Swagger UI:

```text
http://localhost:8000/docs
```

Test routes:

1. `/health` should return status ok.
2. `/equipment-info` should return all classes.
3. `/rag-search` should return relevant chunks.
4. `/ask-ai` should return an AI answer.
5. `/predict` should accept an image. Real prediction requires `sports_model.pth`.

## Frontend Testing

```bash
cd frontend
npm run dev
```

Open every page and test all forms.

## Model Testing

After training, run predictions using `/predict` with images from the test set. Verify that confidence values are reasonable and that top predictions match the input equipment.
