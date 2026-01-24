import tkinter as tk

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
