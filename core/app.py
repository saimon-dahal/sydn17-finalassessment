import tkinter as tk
from PIL import Image, ImageTk
from ui.menu_bar import MenuBar
from ui.dialogs import AboutDialog
from config.config import settings
from ui.status_bar import StatusBar
from ui.control_panel import ControlPanel
from core.file_handler import FileHandler
from tkinter import messagebox
from ui.canvas_display import CanvasDisplay
from core.image_manager import ImageManager
from operations import adjustments

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
            self.image_manager.get_current_image(), self.image_manager.filename
        ):
            self.status_bar.update(f"Saved: {self.image_manager.filename}")

    def save_image_as(self):
        """Save image with new filename"""
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
        if info["width"] > 0:
            self.status_bar.update(
                f"{info['filename']} | {info['width']} × {info['height']} px"
            )
        else:
            self.status_bar.update(info["filename"])


    def handle_slider_change(self, value):
        """Handle slider value changes"""
        if not self.image_manager.has_image():
            return
        
        try:
            # Get current tab
            current_tab = self.control_panel.notebook.select()
            tab_text = self.control_panel.notebook.tab(current_tab, "text")
            
            if tab_text == "Adjust":
                self.preview_adjustments()
        
        except Exception as e:
            print(f"Slider error: {e}")
    def preview_adjustments(self):
        """Preview brightness and contrast adjustments in real-time"""
        # Get slider values
        brightness_val = self.control_panel.brightness_slider.get()
        contrast_val = self.control_panel.contrast_slider.get()
        
        # Update labels
        self.control_panel.brightness_value.config(text=str(int(brightness_val)))
        self.control_panel.contrast_value.config(text=str(int(contrast_val)))
        
        # Apply to original image (not current, for clean preview)
        temp_image = self.image_manager.get_original_image().copy()
        
        # Apply brightness
        if brightness_val != 0:
            temp_image = adjustments.adjust_brightness(temp_image, brightness_val)
        
        # Apply contrast
        if contrast_val != 0:
            temp_image = adjustments.adjust_contrast(temp_image, contrast_val)
        
        # Display preview (don't update history yet)
        self.canvas_display.display_image(temp_image)

    def apply_adjustments(self):
        """Apply and save brightness/contrast adjustments"""
        if not self.image_manager.has_image():
            return
        
        brightness_val = self.control_panel.brightness_slider.get()
        contrast_val = self.control_panel.contrast_slider.get()
        
        if brightness_val == 0 and contrast_val == 0:
            self.status_bar.update("No adjustments to apply")
            return
        
        try:
            # Apply to original
            result = self.image_manager.get_original_image().copy()
            
            if brightness_val != 0:
                result = adjustments.adjust_brightness(result, brightness_val)
            
            if contrast_val != 0:
                result = adjustments.adjust_contrast(result, contrast_val)
            
            # Update image and history
            self.image_manager.update_image(result)
            self.canvas_display.display_image(result)
            self.update_status()
            
            # Reset sliders
            self.control_panel.reset_sliders()
            self.status_bar.update("Adjustments applied")
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply adjustments:\n{str(e)}")
    
    def todo(self):
        print("Placeholder for unwritten features...")

    def on_slider(self, value):
        print(f"Slider: {value}")

    def show_about(self):
        """Show about dialog"""
        AboutDialog.show(self.root)
