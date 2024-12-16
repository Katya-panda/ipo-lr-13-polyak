from PIL import ImageFilter, ImageOps # импорт библиотек для фильтров и операций с изображениями
class ImageProcessor:
    def __init__(self, image):
        self.image = image # сохраняем изображение, переданное из ImageHandler
    def apply_sharpen_filter(self):
        self.image = self.image.filter(ImageFilter.SHARPEN) # применяем фильтр повышения резкости
        print("Фильтр повышения резкости применён.") # печатаем сообщение о применении фильтра
    def add_border(self, border_size):
        self.image = ImageOps.expand(self.image, border=border_size, fill='black') # добавляем рамку вокруг изображения
        print(f"Рамка шириной {border_size} пикселей добавлена.") # печатаем сообщение о добавлении рамки
    def save_processed_image(self, save_path):
        self.image.save(save_path) # сохраняем обработанное изображение
        print(f"Обработанное изображение сохранено в {save_path}.") # печатаем сообщение о сохранении обработанного изображения