import tkinter as tk
from tkinter import messagebox
from core.image_manager import ImageManager
from ui.menu_bar import MenuBar
from ui.status_bar import StatusBar
from ui.control_panel import ControlPanel
from tkinter import filedialog
from PIL import Image, ImageTk
from config.config import settings

class ImageEditorApp:
    def __init__(self, root):
        """Initialize application"""
        self.root = root
        self.setup_window()

        self.image_manager = ImageManager()

        # Image storage
        self.original_image = None
        self.current_image = None
        self.photo_image = None
        self.filename = "No image loaded"

        self.setup_ui()

    def setup_window(self):
        """Configure main window"""
        self.root.title(settings.window.title)
        self.root.geometry(f"{settings.window.width}x{settings.window.height}")
        self.root.configure(bg=settings.colors.background)

    def setup_ui(self):
        """Initialize UI components"""
        self.menu = MenuBar(self.root, {
            'open': self.open_image,
            'save': self.todo,
            'save_as': self.todo,
            'undo': self.todo,
            'redo': self.todo,
            'about': self.todo
        })

        self.create_workspace()

        self.status_bar = StatusBar(self.root)
        self.status_bar.update(self.image_manager.filename)

    def create_workspace(self):
        workspace = tk.Frame(self.root, bg=settings.colors.background)
        workspace.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        workspace.grid_rowconfigure(0, weight=1)
        workspace.grid_columnconfigure(0, weight=3)
        workspace.grid_columnconfigure(1, weight=1)
        
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Canvas
        canvas_frame = tk.Frame(workspace, bg=settings.colors.canvas_background, 
                               relief=tk.RIDGE, bd=1)
        canvas_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
        
        self.canvas = tk.Canvas(canvas_frame, bg=settings.colors.canvas_background, 
                               highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Control Panel
        self.control_panel = ControlPanel(workspace, {
            'button': self.todo,
            'slider': self.on_slider
        })

    def open_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if not path:
            return
        
        self.original_image = Image.open(path)
        self.current_image = self.original_image.copy()
        self.filename = path.split("/")[-1]
        
        self.display_image()
        self.update_status()

    def display_image(self):
        """Show image on canvas"""
        if not self.current_image:
            return
        
        self.canvas.update_idletasks()
        cw = self.canvas.winfo_width()
        ch = self.canvas.winfo_height()
        
        img = self.current_image.copy()
        img.thumbnail((cw, ch), Image.Resampling.LANCZOS)
        
        self.photo_image = ImageTk.PhotoImage(img)
        self.canvas.delete("all")
        
        x = (cw - img.width) // 2
        y = (ch - img.height) // 2
        self.canvas.create_image(x, y, image=self.photo_image, anchor="nw")

    def update_status(self):
        """Update status bar"""
        if self.current_image:
            w, h = self.current_image.size
            self.status_bar.update(f"{self.filename} | {w} × {h} px")
        else:
            self.status_bar.update("No image loaded")

    def todo(self):
        print("Placeholder for unwritten features...")
    def on_slider(self, value):
        print(f"Slider: {value}")