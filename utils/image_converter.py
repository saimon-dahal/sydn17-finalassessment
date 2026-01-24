import cv2
import numpy as np
from PIL import Image


def pil_to_cv2(pil_image):
    """Convert PIL Image to OpenCV format (BGR)."""
    rgb_array = np.array(pil_image)
    bgr_array = cv2.cvtColor(rgb_array, cv2.COLOR_RGB2BGR)
    return bgr_array


def cv2_to_pil(cv2_image):
    """Convert OpenCV image (BGR) to PIL Image format."""
    rgb_array = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_array)
    return pil_image


def ensure_rgb(image):
    """Ensure image is in RGB mode."""
    if image.mode != 'RGB':
        return image.convert('RGB')
    return image