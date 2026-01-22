import tkinter as tk

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SYDN-17 Image Editor")
        self.root.geometry("1000x700")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()