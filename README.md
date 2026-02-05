# Image Editor Application

A Python-based image editing application built with Tkinter, OpenCV, and Pillow. This project allows users to load, edit, and save images with a variety of processing tools.

    Created by SYDN-17 group as a final assessment for HIT-137 Software Now.

## Features

### Image Adjustments
- **Brightness & Contrast**: Real-time slider adjustments.

### Filters
- **Grayscale**: Convert images to black and white.
- **Blur**: Apply Gaussian blur.
- **Edge Detection**: Highlight edges using Canny edge detection.

### Transformations
- **Resize**: Custom width and height resizing (Lanczos resampling).
- **Rotate**: 90°, 180°, and 270° rotation.
- **Flip**: Horizontal and Vertical flipping.

### Workflow Tools
- **Undo/Redo**: Full history support for all operations.
- **Save/Save As**: Export your work properly.

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Open | `Ctrl + O` |
| Save | `Ctrl + S` |
| Save As | `Ctrl + Shift + S` |
| Undo | `Ctrl + Z` |
| Redo | `Ctrl + Y` |

## Requirements

- Python 3.x
- `opencv-python`
- `pillow` (PIL)
- `numpy`

## How to Run

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```
