from tkinter import filedialog, messagebox
from PIL import Image
from config.config import settings

class FileHandler:

    @staticmethod
    def open_file():
        filepath = filedialog.askopenfilename(
            title="Open Image",
            filetypes=settings.file_types.supported_formats
        )

        if not filepath:
            return None, None
        
        try:
            image = Image.open(filepath)
            filename = filepath.split("/")[-1]
            return image, filename
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image:\n{str(e)}")
            return None, None
        
    @staticmethod
    def save_file(image, current_filename=None):
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
        """
        Save image with new filename
        
        Args:
            image: PIL Image object
        
        Returns:
            tuple: (success: bool, filename: str or None)
        """
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
            filename = filepath.split("/")[-1]
            return True, filename
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save image:\n{str(e)}")
            return False, None