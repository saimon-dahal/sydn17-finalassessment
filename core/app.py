import tkinter as tk
from tkinter import messagebox

from config.config import settings

from core.image_manager import ImageManager
from core.file_handler import FileHandler

from ui.menu_bar import MenuBar
from ui.status_bar import StatusBar
from ui.control_panel import ControlPanel
from ui.canvas_display import CanvasDisplay
from ui.dialogs import ResizeDialog, AboutDialog

from operations import adjustments, filters, transforms
from utils.validators import validate_blur_intensity


class ImageEditorApp:
    """Main application controller"""
    
    def __init__(self, root):
        """Initialize application"""
        self.root = root
        self.setup_window()
        
        # Core components
        self.image_manager = ImageManager()
        self.file_handler = FileHandler()
        
        # UI components
        self.menu_bar = None
        self.status_bar = None
        self.control_panel = None
        self.canvas_display = None
        
        self.setup_ui()
    
    def setup_window(self):
        """Configure main window"""
        self.root.title(settings.window.title)
        self.root.geometry(f"{settings.window.width}x{settings.window.height}")
        self.root.configure(bg=settings.colors.background)
    
    def setup_ui(self):
        """Initialize all UI components."""
        self.menu_bar = MenuBar(self.root, {
            'open': self.open_image,
            'save': self.save_image,
            'save_as': self.save_image_as,
            'undo': self.undo,
            'redo': self.redo,
            'about': self.show_about
        })
        
        # Workspace
        self.create_workspace()
        
        # Status bar
        self.status_bar = StatusBar(self.root)
        self.status_bar.update(self.image_manager.filename)
    
    def create_workspace(self):
        """Create main workspace with canvas and control panel"""
        workspace = tk.Frame(self.root, bg=settings.colors.background)
        workspace.grid(row=1, column=0, sticky="nsew", padx=settings.layout.workspace_padding, pady=settings.layout.workspace_padding)
        
        # Configure grid
        workspace.grid_rowconfigure(0, weight=1)
        workspace.grid_columnconfigure(0, weight=settings.layout.canvas_column_weight)
        workspace.grid_columnconfigure(1, weight=settings.layout.panel_column_weight)
        
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Canvas display
        self.canvas_display = CanvasDisplay(workspace)
        
        # Control panel
        self.control_panel = ControlPanel(workspace, {
            'button_click': self.handle_button_click,
            'slider_change': self.handle_slider_change,
            'apply_adjustments': self.apply_adjustments
        })
    
    def open_image(self):
        """Open image file"""
        image, filepath = self.file_handler.open_file()
        
        if image and filepath:
            self.image_manager.load_image(image, filepath)
            self.canvas_display.display_image(self.image_manager.get_current_image())
            self.update_status()
            self.control_panel.reset_sliders()
    
    def save_image(self):
        """Save current image"""
        if not self.image_manager.has_image():
            messagebox.showwarning("Warning", settings.messages.load_image_first)
            return
        
        if self.file_handler.save_file(
            self.image_manager.get_current_image(),
            self.image_manager.filepath
        ):
            self.status_bar.show_save_message(f"Saved: {self.image_manager.filename}")
    
    def save_image_as(self):
        """Save image with new filename"""
        if not self.image_manager.has_image():
            messagebox.showwarning("Warning", settings.messages.load_image_first)
            return
        
        success, filepath = self.file_handler.save_file_as(
            self.image_manager.get_current_image()
        )
        
        if success and filepath:
            # Update path and filename - extract filename for display
            filename = filepath.split("/")[-1]
            self.image_manager.filepath = filepath
            self.image_manager.filename = filename
            
            self.status_bar.show_save_message(f"Saved as: {filename}")
            self.update_status()
    
    def undo(self):
        """Undo last operation"""
        if self.image_manager.undo():
            self.canvas_display.display_image(self.image_manager.get_current_image())
            self.update_status()
        else:
            self.status_bar.update("Nothing to undo")
    
    def redo(self):
        """Redo last undone operation"""
        if self.image_manager.redo():
            self.canvas_display.display_image(self.image_manager.get_current_image())
            self.update_status()
        else:
            self.status_bar.update("Nothing to redo")
    
    def handle_button_click(self, event=None):
        """Handle all button clicks from control panel"""
        if not self.image_manager.has_image():
            messagebox.showwarning("Warning", settings.messages.load_image_first)
            return
        
        # Get button text
        if isinstance(event, str):
            button_text = event
        else:
            widget = event.widget if event else self.root.focus_get()
            if not widget:
                return
            button_text = widget.cget("text")
        
        try:
            current_image = self.image_manager.get_current_image()
            
            # FILTERS
            if button_text == "Grayscale":
                result = filters.apply_grayscale(current_image)
                self.image_manager.update_image(result)
                self.status_bar.update("Applied grayscale filter")
            
            elif button_text == "Blur":
                intensity = validate_blur_intensity(self.control_panel.blur_slider.get())
                result = filters.apply_blur(current_image, intensity)
                self.image_manager.update_image(result)
                self.status_bar.update(f"Applied blur (intensity: {intensity})")
            
            elif button_text == "Edge Detect":
                result = filters.apply_edge_detection(current_image)
                self.image_manager.update_image(result)
                self.status_bar.update("Applied edge detection")
            
            # TRANSFORMS - Rotation
            elif button_text == "90°":
                result = transforms.rotate_image(current_image, 90)
                self.image_manager.update_image(result)
                self.status_bar.update("Rotated 90° clockwise")
            
            elif button_text == "180°":
                result = transforms.rotate_image(current_image, 180)
                self.image_manager.update_image(result)
                self.status_bar.update("Rotated 180°")
            
            elif button_text == "270°":
                result = transforms.rotate_image(current_image, 270)
                self.image_manager.update_image(result)
                self.status_bar.update("Rotated 270° clockwise")
            
            # TRANSFORMS - Flipping
            elif button_text == "Horizontal":
                result = transforms.flip_image(current_image, "horizontal")
                self.image_manager.update_image(result)
                self.status_bar.update("Flipped horizontally")
            
            elif button_text == "Vertical":
                result = transforms.flip_image(current_image, "vertical")
                self.image_manager.update_image(result)
                self.status_bar.update("Flipped vertically")
            
            elif button_text == "Resize":
                try:
                    width = int(self.control_panel.width_entry.get())
                    height = int(self.control_panel.height_entry.get())
                    self.resize_image(width, height)
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid integer values for Width and Height")
                return
            
            # Update display
            self.canvas_display.display_image(self.image_manager.get_current_image())
            self.update_status()
        
        except Exception as e:
            messagebox.showerror("Error", f"Operation failed:\n{str(e)}")
    
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
        temp_image = self.image_manager.get_current_image().copy()
        
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
            messagebox.showwarning("Warning", settings.messages.load_image_first)
            return
        
        brightness_val = self.control_panel.brightness_slider.get()
        contrast_val = self.control_panel.contrast_slider.get()
        
        if brightness_val == 0 and contrast_val == 0:
            self.status_bar.update("No adjustments to apply")
            return
        
        try:
            # Apply to original
            result = self.image_manager.get_current_image().copy()
            
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
    
    def show_resize_dialog(self):
        """Show resize dialog"""
        current_size = self.image_manager.get_current_image().size
        ResizeDialog(self.root, current_size, self.resize_image)
    
    def resize_image(self, width, height):
        """
        Resize image to specified dimensions
        """
        try:
            current_image = self.image_manager.get_current_image()
            result = transforms.resize_image(current_image, width, height)
            self.image_manager.update_image(result)
            self.canvas_display.display_image(result)
            self.update_status()
        
        except Exception as e:
            messagebox.showerror("Error", f"Resize failed:\n{str(e)}")
    
    def show_about(self):
        """Show about dialog"""
        AboutDialog.show(self.root)
    
    def update_status(self):
        """Update status bar with current image info"""
        info = self.image_manager.get_image_info()
        if info['width'] > 0:
            self.status_bar.update(
                f"{info['filename']} | {info['width']} × {info['height']} px"
            )
        else:
            self.status_bar.update(info['filename'])