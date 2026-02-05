
from PIL import Image


def rotate_image(image, angle_degrees):
    """
    Rotate image clockwise by the given angle (in degrees).
    Uses bicubic resampling and expands canvas to avoid cropping.
    """
    try:
        angle = float(angle_degrees)
    except (TypeError, ValueError):
        raise ValueError("Angle must be a number")

    # PIL rotates counter‑clockwise for positive values, so invert for clockwise
    return image.rotate(-angle, expand=True, resample=Image.Resampling.BICUBIC)


def flip_image(image, direction):
    """
    Flip image horizontally or vertically.
    direction: 'horizontal' or 'vertical' (case-insensitive)
    """
    direction = direction.lower()
    if direction == "horizontal":
        return image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    if direction == "vertical":
        return image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    raise ValueError("direction must be 'horizontal' or 'vertical'")


def resize_image(image, width, height):
    """
    Resize image to width x height using high-quality Lanczos resampling.
    """
    return image.resize((int(width), int(height)), Image.Resampling.LANCZOS)


def crop_image(image, left, top, right, bottom):
    """
    Crop the image to the box (left, top, right, bottom).
    Coordinates are clamped to image bounds; raises ValueError if box is invalid.
    """
    w, h = image.size

    try:
        l = max(0, int(left))
        t = max(0, int(top))
        r = min(w, int(right))
        b = min(h, int(bottom))
    except (TypeError, ValueError):
        raise ValueError("Crop values must be integers")

    if l >= r or t >= b:
        raise ValueError("Crop box must have positive width and height")

    return image.crop((l, t, r, b))
