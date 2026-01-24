"""
Image Converter Utilities
==========================
Helper functions for converting between PIL and OpenCV image formats.
"""

import cv2
import numpy as np
from PIL import Image


def pil_to_cv2(pil_image):
    """
    Convert PIL Image to OpenCV format (BGR)
    
    Args:
        pil_image: PIL Image object
    
    Returns:
        NumPy array in BGR format (OpenCV standard)
    """
    # Convert PIL Image to numpy array (RGB)
    rgb_array = np.array(pil_image)
    
    # Convert RGB to BGR (OpenCV uses BGR, not RGB)
    bgr_array = cv2.cvtColor(rgb_array, cv2.COLOR_RGB2BGR)
    
    return bgr_array


def cv2_to_pil(cv2_image):
    """
    Convert OpenCV image (BGR) to PIL Image format
    
    Args:
        cv2_image: NumPy array in BGR format
    
    Returns:
        PIL Image object
    """
    # Convert BGR to RGB
    rgb_array = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
    
    # Convert numpy array to PIL Image
    pil_image = Image.fromarray(rgb_array)
    
    return pil_image


def ensure_rgb(image):
    """
    Ensure image is in RGB mode (convert from RGBA, L, etc.)
    
    Args:
        image: PIL Image object
    
    Returns:
        PIL Image object in RGB mode
    """
    if image.mode != 'RGB':
        return image.convert('RGB')
    return image