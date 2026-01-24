
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
    """Validate and adjust blur intensity to be an odd number."""
    try:
        value = int(intensity)
        
        # Clamp to valid range
        value = max(1, min(15, value))
        
        # Ensure odd number
        if value % 2 == 0:
            value += 1
        
        return value
    
    except (ValueError, TypeError):
        return 5  # Default value


def validate_angle(angle):
    """Validate rotation angle."""
    return angle in [90, 180, 270]


def validate_flip_direction(direction):
    """Validate flip direction."""
    return direction.lower() in ["horizontal", "vertical"]