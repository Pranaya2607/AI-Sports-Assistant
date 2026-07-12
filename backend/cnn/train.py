import argparse
import copy
import json
import random
import ssl
from pathlib import Path
from typing import Dict, Tuple

ssl._create_default_https_context = ssl._create_unverified_context

import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import classification_report, confusion_matrix
from torch.utils.data import DataLoader
from torchvision import datasets, models, transforms
from tqdm import tqdm

BASE_DIR = Path(__file__).resolve().parent
CLASSES_PATH = BASE_DIR / "classes.json"
MODEL_OUTPUT_PATH = BASE_DIR / "sports_model.pth"
METRICS_OUTPUT_PATH = BASE_DIR / "training_metrics.json"
IMAGE_SIZE = 224


def seed_everything(seed: int = 42) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def load_classes() -> list[str]:
    with open(CLASSES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)["classes"]


def create_transforms() -> Dict[str, transforms.Compose]:
    return {
        "train": transforms.Compose([
            transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
            transforms.RandomHorizontalFlip(p=0.5),
            transforms.RandomRotation(15),
            transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
            transforms.RandomAffine(degrees=0, translate=(0.08, 0.08), scale=(0.9, 1.1)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ]),
        "valid": transforms.Compose([
            transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ]),
        "test": transforms.Compose([
            transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ]),
    }


def validate_dataset_structure(data_dir: Path, expected_classes: list[str]) -> None:
    required_splits = ["train", "valid", "test"]
    missing = []
    for split in required_splits:
        split_dir = data_dir / split
        if not split_dir.exists():
            missing.append(str(split_dir))
            continue
        for class_name in expected_classes:
            class_dir = split_dir / class_name
            if not class_dir.exists():
                missing.append(str(class_dir))
    if missing:
        raise FileNotFoundError(
            "Dataset structure is incomplete. Create these folders and add images:\n" + "\n".join(missing[:40])
        )


def create_dataloaders(data_dir: Path, batch_size: int, workers: int) -> Tuple[Dict[str, DataLoader], Dict[str, int], Dict[str, int]]:
    expected_classes = load_classes()
    validate_dataset_structure(data_dir, expected_classes)
    tfms = create_transforms()
    image_datasets = {
        split: datasets.ImageFolder(data_dir / split, transform=tfms[split])
        for split in ["train", "valid", "test"]
    }

    class_to_idx = image_datasets["train"].class_to_idx
    dataset_classes = list(class_to_idx.keys())
    if sorted(dataset_classes) != sorted(expected_classes):
        raise ValueError(
            f"Dataset class folders must match classes.json. Found {dataset_classes}; expected {expected_classes}"
        )

    dataloaders = {
        split: DataLoader(
            image_datasets[split],
            batch_size=batch_size,
            shuffle=(split == "train"),
            num_workers=workers,
            pin_memory=torch.cuda.is_available(),
        )
        for split in ["train", "valid", "test"]
    }
    sizes = {split: len(image_datasets[split]) for split in ["train", "valid", "test"]}
    return dataloaders, sizes, class_to_idx


def build_model(num_classes: int, freeze_backbone: bool = True) -> nn.Module:
    weights = models.MobileNet_V3_Large_Weights.DEFAULT
    model = models.mobilenet_v3_large(weights=weights)
    if freeze_backbone:
        for param in model.features.parameters():
            param.requires_grad = False
    in_features = model.classifier[-1].in_features
    model.classifier[-1] = nn.Linear(in_features, num_classes)
    return model


def run_epoch(model, dataloader, criterion, optimizer, device, phase: str) -> Tuple[float, float]:
    model.train() if phase == "train" else model.eval()
    running_loss = 0.0
    running_corrects = 0
    total = 0

    for inputs, labels in tqdm(dataloader, desc=phase):
        inputs = inputs.to(device)
        labels = labels.to(device)
        optimizer.zero_grad()

        with torch.set_grad_enabled(phase == "train"):
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            _, preds = torch.max(outputs, 1)
            if phase == "train":
                loss.backward()
                optimizer.step()

        running_loss += loss.item() * inputs.size(0)
        running_corrects += torch.sum(preds == labels).item()
        total += labels.size(0)

    epoch_loss = running_loss / max(total, 1)
    epoch_acc = running_corrects / max(total, 1)
    return epoch_loss, epoch_acc


def train_model(data_dir: Path, epochs: int, batch_size: int, lr: float, workers: int, freeze_backbone: bool) -> Dict:
    seed_everything()
    classes = load_classes()
    dataloaders, dataset_sizes, class_to_idx = create_dataloaders(data_dir, batch_size, workers)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = build_model(num_classes=len(classes), freeze_backbone=freeze_backbone).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.AdamW(filter(lambda p: p.requires_grad, model.parameters()), lr=lr, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode="max", factor=0.3, patience=2)

    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0
    history = {"train_loss": [], "train_acc": [], "valid_loss": [], "valid_acc": []}

    for epoch in range(epochs):
        print(f"\nEpoch {epoch + 1}/{epochs}")
        train_loss, train_acc = run_epoch(model, dataloaders["train"], criterion, optimizer, device, "train")
        valid_loss, valid_acc = run_epoch(model, dataloaders["valid"], criterion, optimizer, device, "valid")
        scheduler.step(valid_acc)

        history["train_loss"].append(train_loss)
        history["train_acc"].append(train_acc)
        history["valid_loss"].append(valid_loss)
        history["valid_acc"].append(valid_acc)

        print(f"Train loss={train_loss:.4f} acc={train_acc:.4f}")
        print(f"Valid loss={valid_loss:.4f} acc={valid_acc:.4f}")

        if valid_acc > best_acc:
            best_acc = valid_acc
            best_model_wts = copy.deepcopy(model.state_dict())
            torch.save({
                "model_state_dict": best_model_wts,
                "classes": classes,
                "class_to_idx": class_to_idx,
                "image_size": IMAGE_SIZE,
                "best_valid_accuracy": best_acc,
            }, MODEL_OUTPUT_PATH)
            print(f"Saved new best model to {MODEL_OUTPUT_PATH}")

    model.load_state_dict(best_model_wts)
    test_metrics = evaluate_model(model, dataloaders["test"], classes, device)

    metrics = {
        "dataset_sizes": dataset_sizes,
        "best_valid_accuracy": best_acc,
        "history": history,
        "test_metrics": test_metrics,
        "model_path": str(MODEL_OUTPUT_PATH),
    }
    METRICS_OUTPUT_PATH.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    plot_training_curves(history)
    return metrics


def evaluate_model(model, dataloader, classes, device) -> Dict:
    model.eval()
    y_true = []
    y_pred = []
    with torch.no_grad():
        for inputs, labels in tqdm(dataloader, desc="test"):
            inputs = inputs.to(device)
            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)
            y_true.extend(labels.cpu().numpy().tolist())
            y_pred.extend(preds.cpu().numpy().tolist())

    report = classification_report(y_true, y_pred, target_names=classes, output_dict=True, zero_division=0)
    matrix = confusion_matrix(y_true, y_pred).tolist()
    return {"classification_report": report, "confusion_matrix": matrix}


def plot_training_curves(history: Dict) -> None:
    epochs = range(1, len(history["train_loss"]) + 1)
    plt.figure()
    plt.plot(epochs, history["train_loss"], label="Train Loss")
    plt.plot(epochs, history["valid_loss"], label="Valid Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.savefig(BASE_DIR / "loss_curve.png", bbox_inches="tight")
    plt.close()

    plt.figure()
    plt.plot(epochs, history["train_acc"], label="Train Accuracy")
    plt.plot(epochs, history["valid_acc"], label="Valid Accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.savefig(BASE_DIR / "accuracy_curve.png", bbox_inches="tight")
    plt.close()


def parse_args():
    parser = argparse.ArgumentParser(description="Train MobileNetV3 Large for sports equipment recognition.")
    parser.add_argument("--data-dir", type=str, default="../dataset", help="Dataset directory with train/valid/test folders.")
    parser.add_argument("--epochs", type=int, default=15)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--lr", type=float, default=3e-4)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--unfreeze-backbone", action="store_true", help="Fine-tune entire MobileNetV3 backbone.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    results = train_model(
        data_dir=Path(args.data_dir).resolve(),
        epochs=args.epochs,
        batch_size=args.batch_size,
        lr=args.lr,
        workers=args.workers,
        freeze_backbone=not args.unfreeze_backbone,
    )
    print(json.dumps(results, indent=2))
