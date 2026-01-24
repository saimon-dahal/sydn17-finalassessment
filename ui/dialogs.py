import tkinter as tk
from tkinter import messagebox
from config.config import settings

class AboutDialog:
    """About dialog"""
    
    @staticmethod
    def show(parent):
        """
        Show about dialog
        
        Args:
            parent: Parent window
        """
        messagebox.showinfo(settings.about.title, settings.about.message, parent=parent)