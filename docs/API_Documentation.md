# API Documentation

Base URL: `http://localhost:8000`

## POST `/predict`

Predicts equipment from uploaded image.

Request: multipart form-data

| Field | Type | Description |
|---|---|---|
| file | image | JPG, PNG, or WEBP image |

Response:

```json
{
  "status": "success",
  "equipment": "Football",
  "confidence": 96.42,
  "top_predictions": [],
  "message": "Prediction completed successfully.",
  "ai_summary": "..."
}
```

## GET `/equipment-info?equipment=Football`

Returns local equipment database details and Gemini-generated explanation.

## GET `/recommend-accessories?equipment=Football`

Returns accessories and AI recommendation.

## POST `/size-guide`

```json
{
  "equipment": "Tennis Racket",
  "age": 20,
  "height_cm": 165,
  "weight_kg": 55,
  "skill_level": "beginner",
  "sport_context": "college practice"
}
```

## POST `/maintenance`

```json
{
  "equipment": "Cricket Bat",
  "usage_frequency": "weekly",
  "material": "Kashmir willow",
  "issue": "small toe crack"
}
```

## POST `/condition`

```json
{
  "equipment": "Helmet",
  "observed_damage": "outer shell has a visible crack",
  "age_months": 18,
  "usage_frequency": "weekly"
}
```

## POST `/fake-detection`

```json
{
  "equipment": "Sports Shoes",
  "brand_claimed": "Nike",
  "price": "very low",
  "seller_type": "unknown online seller",
  "observations": "logo looks uneven and no invoice"
}
```

## POST `/ask-ai`

```json
{
  "equipment": "Football",
  "question": "Which accessories should a beginner buy?"
}
```

## POST `/rag-search`

```json
{
  "query": "football size guide",
  "top_k": 4
}
```
