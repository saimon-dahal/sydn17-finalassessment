import tkinter as tk
from tkinter import messagebox
from core.image_manager import ImageManager
from core.file_handler import FileHandler
from ui.menu_bar import MenuBar
from ui.status_bar import StatusBar
from ui.control_panel import ControlPanel
from ui.canvas_display import CanvasDisplay
from tkinter import filedialog
from PIL import Image, ImageTk
from config.config import settings
from ui.dialogs import AboutDialog


class ImageEditorApp:
    def __init__(self, root):
        """Initialize application"""
        self.root = root
        self.setup_window()

        self.image_manager = ImageManager()
        self.file_handler = FileHandler()

        # Image storage
        self.original_image = None
        self.current_image = None
        self.photo_image = None

        self.setup_ui()

    def setup_window(self):
        """Configure main window"""
        self.root.title(settings.window.title)
        self.root.geometry(f"{settings.window.width}x{settings.window.height}")
        self.root.configure(bg=settings.colors.background)

    def setup_ui(self):
        """Initialize UI components"""
        self.menu = MenuBar(
            self.root,
            {
                "open": self.open_image,
                "save": self.save_image,
                "save_as": self.save_image_as,
                "undo": self.todo,
                "redo": self.todo,
                "about": self.show_about,
            },
        )

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

        self.canvas_display = CanvasDisplay(workspace)

        # Control Panel
        self.control_panel = ControlPanel(
            workspace, {"button": self.todo, "slider": self.on_slider}
        )

    def open_image(self):
        """Open image file"""
        image, filename = self.file_handler.open_file()

        if image and filename:
            self.image_manager.load_image(image, filename)
            self.canvas_display.display_image(self.image_manager.get_current_image())
            self.update_status()

    def save_image(self):
        """Save current image"""
        if not self.image_manager.has_image():
            messagebox.showwarning("Warning", settings.messages.load_image_first)
            return
        
        if self.file_handler.save_file(
            self.image_manager.get_current_image(),
            self.image_manager.filename
        ):
            self.status_bar.update(f"Saved: {self.image_manager.filename}")
    def save_image_as(self):
        """Save image with new filename"""`
        if not self.image_manager.has_image():
            messagebox.showwarning("Warning", settings.messages.load_image_first)
            return
        
        success, filename = self.file_handler.save_file_as(
            self.image_manager.get_current_image()
        )
        
        if success and filename:
            self.image_manager.filename = filename
            self.status_bar.update(f"Saved as: {filename}")
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
        """Update status bar with current image info"""
        info = self.image_manager.get_image_info()
        if info['width'] > 0:
            self.status_bar.update(
                f"{info['filename']} | {info['width']} × {info['height']} px"
            )
        else:
            self.status_bar.update(info['filename'])

    def todo(self):
        print("Placeholder for unwritten features...")

    def on_slider(self, value):
        print(f"Slider: {value}")

    def show_about(self):
        """Show about dialog"""
        AboutDialog.show(self.root)
