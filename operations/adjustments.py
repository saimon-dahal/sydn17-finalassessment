
"""
Adjustments Operations
======================
Image adjustment functions: brightness and contrast.

GROUPMATE INSTRUCTIONS:
- Implement the 2 functions below
- Each function receives a PIL Image and returns a PIL Image
- Use the helper functions from utils.image_converter
- Follow the pattern shown in comments
"""

import cv2
from utils.image_converter import pil_to_cv2, cv2_to_pil


def adjust_brightness(image, value):
    """
    Adjust image brightness
    
    Args:
        image: PIL Image object
        value: Brightness adjustment (-100 to 100)
               Negative = darker, Positive = brighter
    
    Returns:
        PIL Image object with adjusted brightness
    
    TODO: Implement brightness adjustment
    
    HINTS:
    - Convert value from -100...100 range to pixel values
      brightness = value * 2.55  (this scales it to 0-255 range)
    - Use cv2.convertScaleAbs(image, alpha=1.0, beta=brightness)
      alpha=1.0 keeps contrast unchanged
      beta=brightness adds/subtracts brightness
    
    PATTERN:
    1. Convert PIL to OpenCV: img_cv = pil_to_cv2(image)
    2. Calculate brightness value
    3. Apply: result = cv2.convertScaleAbs(img_cv, alpha=1.0, beta=brightness)
    4. Convert back: return cv2_to_pil(result)
    """
    # Step 1: Convert PIL to OpenCV
    img_cv = pil_to_cv2(image)
    
    # Step 2: Convert value from -100..100 to 0..255 scale
    brightness = value * 2.55
    
    # Step 3: Apply brightness adjustment
    result = cv2.convertScaleAbs(img_cv, alpha=1.0, beta=brightness)
    
    # Step 4: Convert back to PIL
    return cv2_to_pil(result)


def adjust_contrast(image, value):
    """
    Adjust image contrast
    
    Args:
        image: PIL Image object
        value: Contrast adjustment (-100 to 100)
               Negative = less contrast, Positive = more contrast
    
    Returns:
        PIL Image object with adjusted contrast
    
    TODO: Implement contrast adjustment
    
    HINTS:
    - Convert value from -100...100 to multiplier (alpha)
      Formula: alpha = 1.0 + (value / 100.0)
      Example: value=50 → alpha=1.5 (50% more contrast)
               value=-50 → alpha=0.5 (50% less contrast)
    - Use cv2.convertScaleAbs(image, alpha=alpha, beta=0)
      alpha changes contrast multiplier
      beta=0 means no brightness change
    
    PATTERN:
    1. Convert PIL to OpenCV: img_cv = pil_to_cv2(image)
    2. Calculate alpha: alpha = 1.0 + (value / 100.0)
    3. Apply: result = cv2.convertScaleAbs(img_cv, alpha=alpha, beta=0)
    4. Convert back: return cv2_to_pil(result)
    """
    # YOUR CODE HERE
    return image  # Replace this