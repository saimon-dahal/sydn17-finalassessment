import tkinter as tk
from ui_components import MenuBar, StatusBar, ControlPanel
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SYDN-17 Image Editor")
        self.root.geometry("1000x700")

        # Image storage
        self.original_image = None
        self.current_image = None
        self.photo_image = None
        self.filename = "No image loaded"

        self.setup_ui()
    
    def setup_ui(self):
        self.menu = MenuBar(self.root, {
            'open': self.open_image,
            'save': self.todo,
            'save_as': self.todo,
            'undo': self.todo,
            'redo': self.todo,
            'about': self.todo
        })

        self.create_workspace()

        self.status_bar = StatusBar(self.root)
        self.status_bar.update("No image loaded")

    def create_workspace(self):
        workspace = tk.Frame(self.root, bg="#fafafa")
        workspace.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        workspace.grid_rowconfigure(0, weight=1)
        workspace.grid_columnconfigure(0, weight=3)
        workspace.grid_columnconfigure(1, weight=1)
        
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Canvas
        canvas_frame = tk.Frame(workspace, bg="#ffffff", 
                               relief=tk.RIDGE, bd=1)
        canvas_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
        
        self.canvas = tk.Canvas(canvas_frame, bg="#ffffff", 
                               highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Control Panel
        self.control_panel = ControlPanel(workspace, {
            'button': self.todo,
            'slider': self.on_slider
        })

    def open_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if not path:
            return
        
        self.original_image = Image.open(path)
        self.current_image = self.original_image.copy()
        self.filename = path.split("/")[-1]
        
        self.display_image()
        self.update_status()

    def display_image(self):
        """Show image on canvas"""
        if not self.current_image:
            return
        
        self.canvas.update_idletasks()
        cw = self.canvas.winfo_width()
        ch = self.canvas.winfo_height()
        
        img = self.current_image.copy()
        img.thumbnail((cw, ch), Image.Resampling.LANCZOS)
        
        self.photo_image = ImageTk.PhotoImage(img)
        self.canvas.delete("all")
        
        x = (cw - img.width) // 2
        y = (ch - img.height) // 2
        self.canvas.create_image(x, y, image=self.photo_image, anchor="nw")

    def update_status(self):
        """Update status bar"""
        if self.current_image:
            w, h = self.current_image.size
            self.status_bar.update(f"{self.filename} | {w} × {h} px")
        else:
            self.status_bar.update("No image loaded")

    def todo(self):
        print("Placeholder for unwritten features...")
    def on_slider(self, value):
        print(f"Slider: {value}")
    

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()