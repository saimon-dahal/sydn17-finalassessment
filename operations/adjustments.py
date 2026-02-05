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


def adjust_saturation(image, value):
    """Adjust image saturation. value in range -100..100 (0 = no change)."""
    img_cv = pil_to_cv2(image)
    hsv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2HSV).astype("float32")

    # scale factor: -100 -> 0, 0 -> 1, 100 -> 2
    scale = 1.0 + (float(value) / 100.0)
    h, s, v = cv2.split(hsv)
    s *= scale
    s = np.clip(s, 0, 255)
    hsv_scaled = cv2.merge([h, s, v])
    result = cv2.cvtColor(hsv_scaled.astype("uint8"), cv2.COLOR_HSV2BGR)
    return cv2_to_pil(result)
