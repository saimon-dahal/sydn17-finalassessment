import tkinter as tk
from ui_components import MenuBar
from tkinter import filedialog
from PIL import Image
class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SYDN-17 Image Editor")
        self.root.geometry("1000x700")

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

    def open_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if not path:
            return
        
        self.image = Image.open(path)
        print(f"Image path: {path}")

    def todo(self):
        print("Placeholder for unwritten features...")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()