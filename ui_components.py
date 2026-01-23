import tkinter as tk



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