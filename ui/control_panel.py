import tkinter as tk
from tkinter import ttk
from config.config import settings

class ControlPanel:
    def __init__(self, parent, callbacks):
        """Initialize control panel."""
        self.parent = parent
        self.callbacks = callbacks
        self.create_panel()
    
    def create_panel(self):
        """Create the main panel with notebook."""
        panel = tk.Frame(self.parent)
        panel.grid(row=0, column=1, sticky="nsew")
        
        self.notebook = ttk.Notebook(panel)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create tabs
        self.create_adjust_tab()
        self.create_filters_tab()
        self.create_transform_tab()
    
    def create_adjust_tab(self):
        """Create the Adjust tab with brightness and contrast sliders."""
        tab = tk.Frame(self.notebook)
        self.notebook.add(tab, text="Adjust")
        
        # Brightness section
        tk.Label(tab, text="Brightness", font=("Arial", 10, "bold")).pack(pady=(10, 2))
        
        self.brightness_value = tk.Label(tab, text="0", font=("Arial", 9))
        self.brightness_value.pack()
        
        self.brightness_slider = tk.Scale(
            tab,
            from_=settings.brightness_contrast.min_brightness,
            to=settings.brightness_contrast.max_brightness,
            orient=tk.HORIZONTAL,
            showvalue=0,
            command=self.callbacks.get('slider_change')
        )
        self.brightness_slider.pack(fill=tk.X, padx=10)
        
        # Contrast section
        tk.Label(tab, text="Contrast", font=("Arial", 10, "bold")).pack(pady=(15, 2))
        
        self.contrast_value = tk.Label(tab, text="0", font=("Arial", 9))
        self.contrast_value.pack()
        
        self.contrast_slider = tk.Scale(
            tab,
            from_=settings.brightness_contrast.min_contrast,
            to=settings.brightness_contrast.max_contrast,
            orient=tk.HORIZONTAL,
            showvalue=0,
            command=self.callbacks.get('slider_change')
        )
        self.contrast_slider.pack(fill=tk.X, padx=10)
        
        # Apply button
        tk.Button(
            tab,
            text="Apply Adjustments",
            command=self.callbacks.get('apply_adjustments'),
            bg="#4CAF50",
            fg="white",
            font=("Arial", 9, "bold")
        ).pack(pady=20)
    
    def create_filters_tab(self):
        """Create the Filters tab with filter buttons."""
        tab = tk.Frame(self.notebook)
        self.notebook.add(tab, text="Filters")
        
        # Grayscale button
        tk.Button(
            tab,
            text="Grayscale",
            command=self.callbacks.get('button_click'),
            width=20
        ).pack(pady=10, padx=10)
        
        # Blur section
        tk.Button(
            tab,
            text="Blur",
            command=self.callbacks.get('button_click'),
            width=20
        ).pack(pady=5, padx=10)
        
        tk.Label(tab, text="Blur Intensity", font=("Arial", 9)).pack(pady=(5, 2))
        
        self.blur_slider = tk.Scale(
            tab,
            from_=settings.image_processing.min_blur_intensity,
            to=settings.image_processing.max_blur_intensity,
            orient=tk.HORIZONTAL,
            command=self.callbacks.get('slider_change')
        )
        self.blur_slider.set(settings.image_processing.default_blur_intensity)
        self.blur_slider.pack(fill=tk.X, padx=10)
        
        # Edge detection button
        tk.Button(
            tab,
            text="Edge Detect",
            command=self.callbacks.get('button_click'),
            width=20
        ).pack(pady=10, padx=10)
    
    def create_transform_tab(self):
        """Create the Transform tab with rotation, flip, and resize options."""
        tab = tk.Frame(self.notebook)
        self.notebook.add(tab, text="Transform")
        
        # Rotate section
        tk.Label(tab, text="Rotate", font=("Arial", 10, "bold")).pack(pady=(10, 5))
        
        rotate_frame = tk.Frame(tab)
        rotate_frame.pack()
        
        for angle in ("90°", "180°", "270°"):
            tk.Button(
                rotate_frame,
                text=angle,
                command=self.callbacks.get('button_click'),
                width=6
            ).pack(side=tk.LEFT, padx=2)
        
        # Flip section
        tk.Label(tab, text="Flip", font=("Arial", 10, "bold")).pack(pady=(15, 5))
        
        flip_frame = tk.Frame(tab)
        flip_frame.pack()
        
        tk.Button(
            flip_frame,
            text="Horizontal",
            command=self.callbacks.get('button_click'),
            width=10
        ).pack(side=tk.LEFT, padx=2)
        
        tk.Button(
            flip_frame,
            text="Vertical",
            command=self.callbacks.get('button_click'),
            width=10
        ).pack(side=tk.LEFT, padx=2)
        
        # Resize section
        tk.Label(tab, text="Resize", font=("Arial", 10, "bold")).pack(pady=(15, 5))
        
        resize_frame = tk.Frame(tab)
        resize_frame.pack(pady=5)
        
        tk.Label(resize_frame, text="W:").pack(side=tk.LEFT)
        self.width_entry = tk.Entry(resize_frame, width=5)
        self.width_entry.pack(side=tk.LEFT, padx=5)
        
        tk.Label(resize_frame, text="H:").pack(side=tk.LEFT)
        self.height_entry = tk.Entry(resize_frame, width=5)
        self.height_entry.pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            tab,
            text="Resize",
            command=lambda: self.callbacks.get('button_click')("Resize"),
            width=15
        ).pack(pady=5)
    
    def reset_sliders(self):
        """Reset all sliders to default values."""
        self.brightness_slider.set(0)
        self.contrast_slider.set(0)
        self.blur_slider.set(settings.image_processing.default_blur_intensity)
        self.brightness_value.config(text="0")
        self.contrast_value.config(text="0")