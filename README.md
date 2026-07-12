# AI-Based Sports Equipment Recognition and Recommendation System

A final-year engineering project that detects sports equipment from uploaded images using a PyTorch CNN based on MobileNetV3 Large, then uses RAG with FAISS, Sentence Transformers, and Google Gemini AI to generate equipment details, accessories, size recommendations, maintenance guidance, condition analysis, fake-equipment checks, and AI assistant answers.

## Correct Equipment Classes

1. Cricket Bat
2. Cricket Ball
3. Football
4. Basketball
5. Volleyball
6. Tennis Racket
7. Badminton Racket
8. Shuttlecock
9. Hockey Stick
10. Baseball Bat
11. Baseball Glove
12. Goalkeeper Gloves
13. Helmet
14. Golf Club
15. Sports Shoes

## Architecture

```text
User
  ↓
React Frontend
  ↓
Upload Equipment Image
  ↓
FastAPI Backend
  ↓
Image Preprocessing
  ↓
MobileNetV3 Large CNN
  ↓
Detected Equipment + Confidence
  ↓
FAISS Vector Search over Knowledge Base
  ↓
Gemini AI Generation
  ↓
Frontend Cards and Assistant Responses
```

## Project Structure

```text
AI-Sports-Assistant/
  frontend/
    src/
      pages/
      components/
      styles/
      assets/
  backend/
    api/
    models/
    rag/
    vector_db/
    utils/
    cnn/
      train.py
      predict.py
      classes.json
  dataset/
    train/
    valid/
    test/
  knowledge_base/
  docs/
```

## Setup

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r ../requirements.txt
cp .env.example .env
```

Add your Gemini API key in `backend/.env`:

```env
GEMINI_API_KEY=your_actual_key
```

Build the RAG vector database:

```bash
python rag/build_vector_db.py
```

Run the backend:

```bash
uvicorn main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open:

```text
http://localhost:5173
```

## Training the CNN

Add dataset images using the folder format in `dataset/README.md`, then run:

```bash
cd backend
python cnn/train.py --data-dir ../dataset --epochs 15 --batch-size 16 --lr 0.0003
```

The trained model will be saved as:

```text
backend/cnn/sports_model.pth
```

The backend uses this file for `/predict`. If the file is not available, the API clearly returns that the model has not been trained yet.

## Main Backend APIs

| Method | Route | Purpose |
|---|---|---|
| POST | `/predict` | Predict equipment from image |
| GET | `/equipment-info` | Get equipment information |
| GET | `/recommend-accessories` | Recommend accessories |
| POST | `/size-guide` | Generate size recommendation |
| POST | `/maintenance` | Generate maintenance tips |
| POST | `/condition` | Check equipment condition from text/image context |
| POST | `/fake-detection` | Detect fake/counterfeit warning signs |
| POST | `/ask-ai` | Ask Gemini-powered AI assistant |
| POST | `/rag-search` | Search local RAG knowledge base |

## Documentation

See the `docs/` folder for:

- Installation Guide
- API Documentation
- Architecture Diagram
- Model Training Documentation
- Deployment Guide
- Testing Guide
- Presentation Content
- Viva Questions and Answers
- Future Scope
