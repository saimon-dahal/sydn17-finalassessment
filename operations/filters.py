import cv2
from utils.image_converter import pil_to_cv2, cv2_to_pil

def apply_grayscale(image):
    """
    Apply grayscale filter to the image.
    """
    img_cv= pil_to_cv2(image)
    gray= cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

    result= cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    from PIL import Image
    return Image.fromarray(result)


def apply_blur(image, intensity):
    """
    Apply Gaussian blur to the image.
    """
    # Ensure RGB and convert to OpenCV BGR
    img_cv = pil_to_cv2(image)

    # If intensity is 0, return image unchanged
    if int(intensity) <= 0:
        return image

    # Map slider 1–15 to strong, perceptible kernel sizes 3–31 (odd numbers)
    k_size = max(1, int(intensity))
    # force odd
    if k_size % 2 == 0:
        k_size += 1
    # scale up to make blur visible even on high-res images
    k_size = min(31, k_size * 2 + 1)  # 1->3, 5->11, 10->21, 15->31

    blurred = cv2.GaussianBlur(img_cv, (k_size, k_size), 0)
    return cv2_to_pil(blurred)


def apply_edge_detection(image):
    """
    Apply Canny edge detection.
    """
    img_cv= pil_to_cv2(image)
    #Adjusted Canny thresholds for better visibility on average images
    
    edges= cv2.Canny(img_cv,50, 150)
    # Convert single channel edges to RGB  for consistency
    result= cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    from PIL import Image
    return Image.fromarray(result)
    

    
