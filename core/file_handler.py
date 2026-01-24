from tkinter import filedialog, messagebox
from PIL import Image
from config.config import settings


class FileHandler:
    """Manages file operations for images"""
    
    @staticmethod
    def open_file():
        """Open file dialog and load image."""
        filepath = filedialog.askopenfilename(
            title="Open Image",
            filetypes=settings.file_types.supported_formats
        )
        
        if not filepath:
            return None, None
        
        try:
            image = Image.open(filepath)
            return image, filepath
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image:\n{str(e)}")
            return None, None
    
    @staticmethod
    def save_file(image, current_filename=None):
        """Save image (overwrite if filename exists)."""
        if not image:
            messagebox.showwarning("Warning", "No image to save!")
            return False
        
        # If no filename, use save as
        if not current_filename or current_filename == "No image loaded":
            return FileHandler.save_file_as(image)
        
        try:
            image.save(current_filename)
            return True
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save image:\n{str(e)}")
            return False
    
    @staticmethod
    def save_file_as(image):
        """Save image with new filename."""
        if not image:
            messagebox.showwarning("Warning", "No image to save!")
            return False, None
        
        filepath = filedialog.asksaveasfilename(
            title="Save Image As",
            defaultextension=settings.file_types.default_save_extension,
            filetypes=settings.file_types.save_formats
        )
        
        if not filepath:
            return False, None
        
        try:
            image.save(filepath)
            return True, filepath
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save image:\n{str(e)}")
            return False, None