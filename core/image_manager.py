"""Image Manager: Manages image state, history, and metadata."""

from PIL import Image
from config.config import settings


class ImageManager:
    """Manages image state and history for undo/redo functionality"""
    
    def __init__(self):
        self.original_image = None
        self.current_image = None
        self.filepath = None
        self.filename = settings.messages.no_image
        self.history = []
        self.history_index = -1
    
    def load_image(self, image, filepath):
        """Load a new image and reset history."""
        self.original_image = image.copy()
        self.current_image = image.copy()
        self.filepath = filepath
        self.filename = filepath.split("/")[-1] if filepath else settings.messages.no_image
        
        # Reset history with initial state
        self.history = [self.current_image.copy()]
        self.history_index = 0
    
    def update_image(self, image):
        """Update current image and add to history."""
        self.current_image = image.copy()
        self.add_to_history()
    
    def add_to_history(self):
        """Add current image state to history for undo/redo"""
        if not self.current_image:
            return
        
        # Remove any future states if we're not at the end
        self.history = self.history[:self.history_index + 1]
        
        # Add new state
        self.history.append(self.current_image.copy())
        self.history_index += 1
        
        # Limit history size
        if len(self.history) > settings.image_processing.max_undo_history:
            self.history.pop(0)
            self.history_index -= 1
    
    def undo(self):
        """Undo last operation."""
        if self.can_undo():
            self.history_index -= 1
            self.current_image = self.history[self.history_index].copy()
            return True
        return False
    
    def redo(self):
        """Redo last undone operation."""
        if self.can_redo():
            self.history_index += 1
            self.current_image = self.history[self.history_index].copy()
            return True
        return False
    
    def can_undo(self):
        """Check if undo is available"""
        return self.history_index > 0
    
    def can_redo(self):
        """Check if redo is available"""
        return self.history_index < len(self.history) - 1
    
    def get_current_image(self):
        """Get the current image"""
        return self.current_image
    
    def get_original_image(self):
        """Get the original image"""
        return self.original_image
    
    def has_image(self):
        """Check if an image is loaded"""
        return self.current_image is not None
    
    def get_image_info(self):
        """Get current image information."""
        if not self.current_image:
            return {
                'filename': settings.messages.no_image,
                'width': 0,
                'height': 0
            }
        
        width, height = self.current_image.size
        return {
            'filename': self.filename,
            'width': width,
            'height': height
        }
    
    def reset(self):
        """Reset to original image"""
        if self.original_image:
            self.current_image = self.original_image.copy()
            self.history = [self.current_image.copy()]
            self.history_index = 0
            return True
        return False