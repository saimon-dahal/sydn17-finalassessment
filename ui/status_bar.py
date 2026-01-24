import tkinter as tk
from config.config import settings


class StatusBar:
    """Creates and manages the status bar"""

    def __init__(self, parent):
        self.parent = parent
        self.create_status_bar()

    def create_status_bar(self):
        status_bar = tk.Frame(
            self.parent, bg=settings.colors.status_bar_background, height=25
        )
        status_bar.grid(row=2, column=0, sticky="ew")
        status_bar.grid_propagate(False)

        self.status_label = tk.Label(
            status_bar,
            text="",
            anchor=tk.W,
            padx=10,
            bg=settings.colors.status_bar_background,
            fg=settings.colors.status_bar_foreground,
        )
        self.status_label.pack(fill=tk.BOTH)

    def update(self, text):
        """Update status bar text"""
        self.status_label.config(text=text)
        
    def clear(self):
        """Clear status bar text"""
        self.status_label.config(text="")