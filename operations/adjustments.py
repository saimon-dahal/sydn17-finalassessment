import cv2
import numpy as np
from PIL import Image
from utils.image_converter import pil_to_cv2, cv2_to_pil


def adjust_brightness(image, value):
    """Adjust image brightness."""
    img_cv = pil_to_cv2(image)
    # Reduced sensitivity: straight mapping matches slider -100 to 100
    brightness = value
    result = cv2.convertScaleAbs(img_cv, alpha=1.0, beta=brightness)
    return cv2_to_pil(result)


def adjust_contrast(image, value):
    """Adjust image contrast."""
    img_cv = pil_to_cv2(image)
    # Reduced sensitivity: max 1.5x contrast instead of 2.0x
    alpha = 1.0 + (value / 200.0)
    result = cv2.convertScaleAbs(img_cv, alpha=alpha, beta=0)
    return cv2_to_pil(result)