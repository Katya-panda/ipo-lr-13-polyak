from PIL import Image # импорт библиотеки Pillow для работы с изображениями
class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path # сохраняем путь к изображению
        self.image = None # инициализируем переменную для хранения изображения
    def load_image(self):
        self.image = Image.open(self.image_path) # открываем изображение
        print(f"Изображение {self.image_path} загружено.") # печатаем сообщение о загрузке
    def save_image(self, save_path):
        self.image.save(save_path) # сохраняем изображение по указанному пути
        print(f"Изображение сохранено в {save_path}.") # печатаем сообщение о сохранении
    def resize_image(self, size):
        self.image = self.image.resize(size) # изменяем размер изображения
        print(f"Изображение изменено до размера {size}.") # печатаем сообщение об изменении размера
    def convert_to_jpg(self, save_path):
        self.image = self.image.convert("RGB") # преобразуем изображение в формат RGB
        save_path = save_path.replace(".png", ".jpg") # меняем расширение файла на JPG
        self.save_image(save_path) # сохраняем изображение в формате JPG
        print(f"Изображение преобразовано в формат JPG и сохранено в {save_path}.") # печатаем сообщение о преобразовании
    def rotate_image(self, angle):
        self.image = self.image.rotate(angle, expand=True) # поворачиваем изображение на указанный угол с расширением
        print(f"Изображение повёрнуто на {angle} градусов.") # печатаем сообщение о повороте
    def pass_to_processor(self):
        return self.image # возвращаем изображение для дальнейшей обработки