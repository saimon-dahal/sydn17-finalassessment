
from PIL import Image


def rotate_image(image):
    return image


def flip_image(image):
    return image


def resize_image(image, width, height):
    return image.resize((int(width), int(height)), Image.Resampling.LANCZOS)