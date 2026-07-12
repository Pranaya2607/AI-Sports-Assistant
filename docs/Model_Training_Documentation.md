# Model Training Documentation

## CNN Algorithm

The project uses MobileNetV3 Large with transfer learning. MobileNetV3 is a lightweight convolutional neural network suitable for efficient image classification. Transfer learning uses pretrained ImageNet features and replaces the final classifier layer with a 15-class sports equipment classifier.

## Classes

The model detects equipment, not sports activities:

- Cricket Bat
- Cricket Ball
- Football
- Basketball
- Volleyball
- Tennis Racket
- Badminton Racket
- Shuttlecock
- Hockey Stick
- Baseball Bat
- Baseball Glove
- Goalkeeper Gloves
- Helmet
- Golf Club
- Sports Shoes

## Dataset Format

```text
dataset/train/<class_name>/image.jpg
dataset/valid/<class_name>/image.jpg
dataset/test/<class_name>/image.jpg
```

## Training Steps

1. Load class labels from `classes.json`.
2. Validate dataset folder structure.
3. Apply data augmentation to training images.
4. Load pretrained MobileNetV3 Large.
5. Replace final layer with a 15-class classifier.
6. Train using CrossEntropyLoss and AdamW optimizer.
7. Validate after each epoch.
8. Save the best model as `sports_model.pth`.
9. Evaluate on the test dataset.
10. Save loss and accuracy curves.

## Command

```bash
cd backend
python cnn/train.py --data-dir ../dataset --epochs 15 --batch-size 16 --lr 0.0003
```

## Outputs

- `backend/cnn/sports_model.pth`
- `backend/cnn/training_metrics.json`
- `backend/cnn/loss_curve.png`
- `backend/cnn/accuracy_curve.png`
