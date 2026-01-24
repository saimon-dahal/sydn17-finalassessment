import tkinter as tk

from tkinter import ttk
from config.config import settings
class ControlPanel:
    """Creates and manages the tabbed control panel"""
    def __init__(self, parent, callbacks):
        self.parent = parent
        self.callbacks = callbacks
        self.create_panel()
    
    def create_panel(self):
        panel = tk.Frame(self.parent)
        panel.grid(row=0, column=1, sticky="nsew")
        
        self.notebook = ttk.Notebook(panel)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.create_adjust_tab()
        self.create_filters_tab()
        self.create_transform_tab()
    
    def create_adjust_tab(self):
        tab = tk.Frame(self.notebook)
        self.notebook.add(tab, text="Adjust")
        
        # Brightness
        tk.Label(tab, text="Brightness").pack(pady=(10, 2))
        self.brightness_value = tk.Label(tab, text="0", font=("Arial", 9))
        self.brightness_value.pack()
        
        self.brightness_slider = tk.Scale(
            tab, from_=settings.brightness_contrast.min_brightness, to=settings.brightness_contrast.max_brightness,
            orient=tk.HORIZONTAL,
            showvalue=0,
            command=self.callbacks.get('slider_change')
        )
        self.brightness_slider.pack(fill=tk.X, padx=10)
        
        # Contrast
        tk.Label(tab, text="Contrast").pack(pady=(15, 2))
        self.contrast_value = tk.Label(tab, text="0")
        self.contrast_value.pack()
        
        self.contrast_slider = tk.Scale(
            tab, from_=settings.brightness_contrast.min_contrast, to=settings.brightness_contrast.max_contrast,
            orient=tk.HORIZONTAL,
            showvalue=0,
            command=self.callbacks.get('slider_change')
        )
        self.contrast_slider.pack(fill=tk.X, padx=10)

        tk.Button(
            tab,
            text="Apply Adjustments",
            command=self.callbacks.get('apply_adjustments'),
            bg="#4CAF50",
            fg="white",
            font=("Arial", 9, "bold")
        ).pack(pady=20)
    
    def create_filters_tab(self):
        tab = tk.Frame(self.notebook)
        self.notebook.add(tab, text="Filters")
        
        tk.Button(tab, text="Grayscale",
                  command=self.callbacks['button']).pack(pady=5, padx=10)
        
        tk.Button(tab, text="Blur",
                  command=self.callbacks['button']).pack(pady=5, padx=10)
        
        tk.Label(tab, text="Blur Intensity").pack(pady=(5, 2))
        self.blur_slider = tk.Scale(
            tab, from_=1, to=15,
            orient=tk.HORIZONTAL,
            command=self.callbacks['slider']
        )
        self.blur_slider.set(5)
        self.blur_slider.pack(fill=tk.X, padx=10)
        
        tk.Button(tab, text="Edge Detect",
                  command=self.callbacks['button']).pack(pady=5, padx=10)
    
    def create_transform_tab(self):
        tab = tk.Frame(self.notebook)
        self.notebook.add(tab, text="Transform")
        
        # Rotate
        tk.Label(tab, text="Rotate").pack(pady=(10, 5))
        rotate_frame = tk.Frame(tab)
        rotate_frame.pack()
        
        for angle in ("90°", "180°", "270°"):
            tk.Button(
                rotate_frame, text=angle,
                command=self.callbacks['button']
            ).pack(side=tk.LEFT, padx=2)
        
        # Flip
        tk.Label(tab, text="Flip").pack(pady=(15, 5))
        flip_frame = tk.Frame(tab)
        flip_frame.pack()
        
        tk.Button(flip_frame, text="Horizontal",
                  command=self.callbacks['button']).pack(side=tk.LEFT, padx=2)
        tk.Button(flip_frame, text="Vertical",
                  command=self.callbacks['button']).pack(side=tk.LEFT, padx=2)
        
        # Resize
        tk.Label(tab, text="Resize").pack(pady=(15, 5))
        tk.Button(tab, text="Resize Image",
                  command=self.callbacks['button']).pack(pady=5)
    def reset_sliders(self):
        """Reset all sliders to default values"""
        self.brightness_slider.set(0)
        self.contrast_slider.set(0)
        self.blur_slider.set(settings.image_processing.default_blur_intensity)
        self.brightness_value.config(text="0")
        self.contrast_value.config(text="0")