import tkinter as tk
from PIL import Image, ImageTk
from config.config import settings


class CanvasDisplay:
    """Manages canvas for image display."""
    
    def __init__(self, parent):
        """Initialize canvas display."""
        self.parent = parent
        self.canvas = None
        self.photo_image = None
        self.create_canvas()
    
    def create_canvas(self):
        """Create the canvas widget."""
        canvas_frame = tk.Frame(
            self.parent,
            bg=settings.colors.canvas_background,
            relief=tk.RIDGE,
            bd=1
        )
        canvas_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
        
        self.canvas = tk.Canvas(
            canvas_frame,
            bg=settings.colors.canvas_background,
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<Configure>', lambda e: self.on_resize())
        self.show_placeholder()
    
    def on_resize(self):
        """Handle canvas resize."""
        if not self.photo_image:
            self.show_placeholder()
    
    def display_image(self, image):
        """Display image on canvas with proper scaling."""
        if not image:
            return
        
        # Update canvas dimensions
        self.canvas.update_idletasks()
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        # Avoid division by zero
        if canvas_width <= 1 or canvas_height <= 1:
            return
        
        # Create a copy and scale it to fit canvas
        display_image = image.copy()
        max_width = canvas_width - settings.layout.canvas_padding
        max_height = canvas_height - settings.layout.canvas_padding
        display_image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        
        # Convert to PhotoImage
        self.photo_image = ImageTk.PhotoImage(display_image)
        
        # Clear canvas and draw image
        self.canvas.delete("all")
        
        # Center the image
        x = (canvas_width - display_image.width) // 2
        y = (canvas_height - display_image.height) // 2
        
        self.canvas.create_image(x, y, image=self.photo_image, anchor="nw")
    
    def clear(self):
        """Clear the canvas."""
        self.canvas.delete("all")
        self.photo_image = None
        self.show_placeholder()

    def show_placeholder(self):
        """Display placeholder text when no image is loaded."""
        self.canvas.delete("all")
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        # Default dimensions if canvas not yet rendered
        if width <= 1: width = 600
        if height <= 1: height = 400
            
        self.canvas.create_text(
            width // 2,
            height // 2,
            text="Please load an image",
            fill="gray",
            font=("Arial", 14)
        )
    
    def get_canvas(self):
        """Get the canvas widget."""
        return self.canvas