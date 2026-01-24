import tkinter as tk
from tkinter import messagebox
from config.config import settings


class ResizeDialog:
    """Dialog for resizing images."""
    
    def __init__(self, parent, current_size, callback):
        """Initialize resize dialog."""
        self.callback = callback
        self.result = None
        
        # Create dialog
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Resize Image")
        self.dialog.geometry("300x150")
        self.dialog.resizable(False, False)
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Current size label
        tk.Label(
            self.dialog,
            text=f"Current size: {current_size[0]} × {current_size[1]} px",
            font=("Arial", 9)
        ).pack(pady=10)
        
        # Input frame
        input_frame = tk.Frame(self.dialog)
        input_frame.pack(pady=10)
        
        # Width input
        tk.Label(input_frame, text="Width:").grid(row=0, column=0, padx=5, pady=5)
        self.width_entry = tk.Entry(input_frame, width=10)
        self.width_entry.insert(0, str(current_size[0]))
        self.width_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Height input
        tk.Label(input_frame, text="Height:").grid(row=1, column=0, padx=5, pady=5)
        self.height_entry = tk.Entry(input_frame, width=10)
        self.height_entry.insert(0, str(current_size[1]))
        self.height_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Buttons
        button_frame = tk.Frame(self.dialog)
        button_frame.pack(pady=10)
        
        tk.Button(
            button_frame,
            text="Apply",
            command=self.apply,
            width=10,
            bg="#4CAF50",
            fg="white"
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="Cancel",
            command=self.dialog.destroy,
            width=10
        ).pack(side=tk.LEFT, padx=5)
        
        # Center dialog
        self.dialog.update_idletasks()
        x = (parent.winfo_width() // 2) - (self.dialog.winfo_width() // 2) + parent.winfo_x()
        y = (parent.winfo_height() // 2) - (self.dialog.winfo_height() // 2) + parent.winfo_y()
        self.dialog.geometry(f"+{x}+{y}")
    
    def apply(self):
        """Validate and apply resize."""
        try:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
            
            if width <= 0 or height <= 0:
                messagebox.showerror(
                    "Invalid Input",
                    "Width and height must be positive numbers!",
                    parent=self.dialog
                )
                return
            
            self.result = (width, height)
            self.callback(width, height)
            self.dialog.destroy()
        
        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter valid numbers for width and height!",
                parent=self.dialog
            )


class AboutDialog:
    """About dialog."""
    
    @staticmethod
    def show(parent):
        """Show about dialog."""
        messagebox.showinfo(settings.about.title, settings.about.message, parent=parent)