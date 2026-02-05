
from PIL import Image


def rotate_image(image, angle):
    """
    Rotate image by angle.
    """
    return image.rotate(-float(angle), expand=True)
    

def flip_image(image, direction):
    """
    Flip image horizontally or vertically
    """
    if direction == "horizontal":
        return image.transpose(Image.Flip_Left_Right)
    
    elif direction == "vertical":
        return image.transpose(Image.Flip_Top_Bottom)
    
    return image


def resize_image(image, width, height):
    return image.resize((int(width), int(height)), Image.Resampling.LANCZOS)
