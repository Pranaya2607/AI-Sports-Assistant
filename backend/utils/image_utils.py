from io import BytesIO
from PIL import Image

ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/jpg", "image/png", "image/webp"}

def validate_image_type(content_type: str) -> None:
    if content_type not in ALLOWED_IMAGE_TYPES:
        raise ValueError("Only JPG, PNG, and WEBP images are supported.")

def read_image_from_bytes(data: bytes) -> Image.Image:
    image = Image.open(BytesIO(data)).convert("RGB")
    return image
