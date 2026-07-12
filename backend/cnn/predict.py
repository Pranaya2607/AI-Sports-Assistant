import json
from pathlib import Path
from typing import Dict, List, Tuple

import torch
import torch.nn as nn
from PIL import Image
from torchvision import models, transforms

from utils.config import settings

IMAGE_SIZE = 224

class SportsEquipmentPredictor:
    def __init__(self, model_path: Path | None = None, classes_path: Path | None = None):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model_path = model_path or settings.resolved_model_path
        self.classes_path = classes_path or settings.resolved_classes_path
        self.classes = self._load_classes()
        self.model = self._build_model(num_classes=len(self.classes))
        self.transform = self._build_transform()
        self.is_trained_model_loaded = False
        self.load_model()

    def _load_classes(self) -> List[str]:
        with open(self.classes_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return sorted(data["classes"])

    def _build_model(self, num_classes: int) -> nn.Module:
        model = models.mobilenet_v3_large(weights=None)
        in_features = model.classifier[-1].in_features
        model.classifier[-1] = nn.Linear(in_features, num_classes)
        return model.to(self.device)

    def _build_transform(self):
        return transforms.Compose([
            transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def load_model(self) -> None:
        if not self.model_path.exists():
            self.model.eval()
            self.is_trained_model_loaded = False
            return
        checkpoint = torch.load(self.model_path, map_location=self.device)
        if isinstance(checkpoint, dict) and "model_state_dict" in checkpoint:
            self.model.load_state_dict(checkpoint["model_state_dict"])
        else:
            self.model.load_state_dict(checkpoint)
        self.model.eval()
        self.is_trained_model_loaded = True

    @torch.no_grad()
    def predict(self, image: Image.Image, top_k: int = 5) -> Dict:
        if not self.is_trained_model_loaded:
            self.load_model()
            
        if not self.is_trained_model_loaded:
            return {
                "status": "model_not_trained",
                "equipment": None,
                "confidence": 0.0,
                "top_predictions": [],
                "message": "sports_model.pth is not available. Train the CNN using backend/cnn/train.py before using real prediction.",
            }

        tensor = self.transform(image).unsqueeze(0).to(self.device)
        logits = self.model(tensor)
        probabilities = torch.softmax(logits, dim=1).squeeze(0)
        values, indices = torch.topk(probabilities, k=min(top_k, len(self.classes)))

        top_predictions = []
        for value, idx in zip(values.cpu().tolist(), indices.cpu().tolist()):
            top_predictions.append({
                "equipment": self.classes[idx],
                "confidence": round(float(value) * 100, 2),
            })

        best = top_predictions[0]
        
        # Confidence Threshold Calibration
        if best["confidence"] < 50.0:
            return {
                "status": "success",
                "equipment": "Unknown Equipment",
                "confidence": best["confidence"],
                "top_predictions": top_predictions,
                "message": f"Low confidence ({best['confidence']}%). Please ensure the image clearly shows one of the 15 supported items.",
            }
        return {
            "status": "success",
            "equipment": best["equipment"],
            "confidence": best["confidence"],
            "top_predictions": top_predictions,
            "message": "Prediction completed successfully.",
        }

_predictor: SportsEquipmentPredictor | None = None

def get_predictor() -> SportsEquipmentPredictor:
    global _predictor
    if _predictor is None:
        _predictor = SportsEquipmentPredictor()
    return _predictor
