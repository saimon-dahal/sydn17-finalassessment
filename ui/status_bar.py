import tkinter as tk
from config.config import settings


class StatusBar:
    """Creates and manages the status bar."""
    
    def __init__(self, parent):
        """Initialize status bar."""
        self.parent = parent
        self.create_status_bar()
    
    def create_status_bar(self):
        """Create the status bar widget."""
        status_frame = tk.Frame(
            self.parent,
            bg=settings.colors.status_bar_background,
            height=25
        )
        status_frame.grid(row=2, column=0, sticky="ew")
        status_frame.grid_propagate(False)
        
        self.status_label = tk.Label(
            status_frame,
            text="",
            bg=settings.colors.status_bar_background,
            fg=settings.colors.status_bar_foreground,
            anchor=tk.W,
            padx=10
        )
        self.status_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.right_label = tk.Label(
            status_frame,
            text="",
            bg=settings.colors.status_bar_background,
            fg=settings.colors.status_bar_foreground,
            anchor=tk.E,
            padx=10
        )
        self.right_label.pack(side=tk.RIGHT)
    
    def update(self, text):
        """Update status bar text."""
        self.status_label.config(text=text)
        
    def show_save_message(self, text):
        """Show message on the right side."""
        self.right_label.config(text=text)
        # Auto-clear after 3 seconds
        self.parent.after(3000, lambda: self.right_label.config(text=""))
    
    def clear(self):
        """Clear status bar text."""
        self.status_label.config(text="")
        self.right_label.config(text="")