# Deployment Guide

## Backend Deployment

Recommended platforms:

- Render
- Railway
- Azure App Service
- AWS EC2

Start command:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Environment variables:

```env
GEMINI_API_KEY=your_actual_key
FRONTEND_ORIGIN=https://your-frontend-domain.com
```

Before deployment, build the vector database:

```bash
python rag/build_vector_db.py
```

Upload `sports_model.pth` after training.

## Frontend Deployment

Recommended platforms:

- Vercel
- Netlify
- Render Static Site

Build command:

```bash
npm run build
```

Set frontend environment variable:

```env
VITE_API_BASE_URL=https://your-backend-url.com
```
