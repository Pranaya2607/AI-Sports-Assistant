from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

class PredictionResponse(BaseModel):
    status: str
    equipment: Optional[str] = None
    confidence: float = 0.0
    top_predictions: List[Dict[str, Any]] = Field(default_factory=list)
    message: str

class EquipmentQuery(BaseModel):
    equipment: str

class SizeGuideRequest(BaseModel):
    equipment: str
    age: Optional[int] = None
    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None
    skill_level: str = "beginner"
    sport_context: Optional[str] = None

class MaintenanceRequest(BaseModel):
    equipment: str
    usage_frequency: str = "weekly"
    material: Optional[str] = None
    issue: Optional[str] = None

class ConditionRequest(BaseModel):
    equipment: str
    observed_damage: str
    age_months: Optional[int] = None
    usage_frequency: str = "weekly"

class FakeDetectionRequest(BaseModel):
    equipment: str
    brand_claimed: Optional[str] = None
    price: Optional[str] = None
    seller_type: Optional[str] = None
    observations: str

class AskAIRequest(BaseModel):
    question: str
    equipment: Optional[str] = None

class RagSearchRequest(BaseModel):
    query: str
    top_k: int = 4

class GeminiCardResponse(BaseModel):
    title: str
    content: str
    sources: List[str] = Field(default_factory=list)
