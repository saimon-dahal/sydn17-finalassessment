import tkinter as tk
from ui_components import MenuBar

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SYDN-17 Image Editor")
        self.root.geometry("1000x700")

        self.setup_ui()
    
    def setup_ui(self):
        self.menu = MenuBar(self.root, {
            'open': self.todo,
            'save': self.todo,
            'save_as': self.todo,
            'undo': self.todo,
            'redo': self.todo,
            'about': self.todo
        })
    
    def todo(self):
        print("Placeholder for unwritten features...")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()