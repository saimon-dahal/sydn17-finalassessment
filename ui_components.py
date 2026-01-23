import tkinter as tk

from tkinter import ttk

class MenuBar:
    """Creates and manages the menu bar"""
    def __init__(self, root, callbacks):
        self.root = root
        self.callbacks = callbacks
        self.create_menu()
    
    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.callbacks['open'])
        file_menu.add_command(label="Save", command=self.callbacks['save'])
        file_menu.add_command(label="Save As", command=self.callbacks['save_as'])
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.callbacks['undo'])
        edit_menu.add_command(label="Redo", command=self.callbacks['redo'])
        menubar.add_cascade(label="Edit", menu=edit_menu)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.callbacks['about'])
        menubar.add_cascade(label="Help", menu=help_menu)

class StatusBar:
    """Creates and manages the status bar"""
    def __init__(self, parent):
        self.parent = parent
        self.create_status_bar()
    
    def create_status_bar(self):
        status_bar = tk.Frame(self.parent, bg="#e8e8e8", height=25)
        status_bar.grid(row=2, column=0, sticky="ew")
        status_bar.grid_propagate(False)
        
        self.status_label = tk.Label(status_bar, text="", bg="#e8e8e8", 
                                     anchor=tk.W, padx=10, fg="#000000")
        self.status_label.pack(fill=tk.BOTH)
    
    def update(self, text):
        """Update status bar text"""
        self.status_label.config(text=text)

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
        self.brightness_value = tk.Label(tab, text="0")
        self.brightness_value.pack()
        
        self.brightness_slider = tk.Scale(
            tab, from_=-100, to=100,
            orient=tk.HORIZONTAL,
            showvalue=0,
            command=self.callbacks['slider']
        )
        self.brightness_slider.pack(fill=tk.X, padx=10)
        
        # Contrast
        tk.Label(tab, text="Contrast").pack(pady=(15, 2))
        self.contrast_value = tk.Label(tab, text="0")
        self.contrast_value.pack()
        
        self.contrast_slider = tk.Scale(
            tab, from_=-100, to=100,
            orient=tk.HORIZONTAL,
            showvalue=0,
            command=self.callbacks['slider']
        )
        self.contrast_slider.pack(fill=tk.X, padx=10)
    
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
