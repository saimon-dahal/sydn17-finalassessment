
def validate_dimensions(width, height):
    """Validate image dimensions."""
    try:
        w = int(width)
        h = int(height)
        
        if w <= 0 or h <= 0:
            return False, "Dimensions must be positive numbers"
        
        if w > 10000 or h > 10000:
            return False, "Dimensions too large (max 10000px)"
        
        return True, None
    
    except (ValueError, TypeError):
        return False, "Invalid number format"


def validate_blur_intensity(intensity):
    """Validate blur intensity slider input."""
    try:
        value = int(intensity)
        # Clamp to 0-15; 0 means no blur
        value = max(0, min(15, value))
        return value
    except (ValueError, TypeError):
        return 0  # Default to 0 blur on invalid input


def validate_angle(angle):
    """Validate rotation angle."""
    return angle in [90, 180, 270]


def validate_flip_direction(direction):
    """Validate flip direction."""
    return direction.lower() in ["horizontal", "vertical"]
