from PIL import Image
from config.config import settings


class ImageManager:
    def __init__(self):
        self.original_image = None
        self.current_image = None
        self.filename = settings.messages.no_image

    def load_image(self, image, filename):
        self.original_image = image.copy()
        self.current_image = image.copy()
        self.filename = filename

    def udpate_image(self, image):
        self.current_image = image.copy()

    def get_image_info(self):
        if not self.current_image:
            return {"filename": settings.message.no_image, "width": 0, "height": 0}

        width, height = self.current_image.size
        return {"filename": self.filename, "width": width, "height": height}
