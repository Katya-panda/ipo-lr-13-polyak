from image_handler import ImageHandler # импортируем класс ImageHandler из модуля image_handler
from image_processor import ImageProcessor # импортируем класс ImageProcessor из модуля image_processor
def main():
    # запрашиваем у пользователя путь к изображению и сохраняем его в переменную image_path
    image_path = input("Введите путь к изображению: ")
    # создаем объект класса ImageHandler, передав ему путь к изображению
    ih = ImageHandler(image_path)
    # загружаем изображение с помощью метода load_image
    ih.load_image()
    # преобразуем изображение в формат JPG и сохраняем его в файл output.jpg
    ih.convert_to_jpg("output.jpg") 
    # поворачиваем изображение на 45 градусов
    ih.rotate_image(45)
    # создаем объект класса ImageProcessor, передав ему изображение из ImageHandler для дальнейшей обработки
    ip = ImageProcessor(ih.pass_to_processor())
    # применяем фильтр повышения резкости к изображению
    ip.apply_sharpen_filter()
    # добавляем рамку шириной 15 пикселей вокруг изображения
    ip.add_border(15)
    # сохраняем обработанное изображение в файл output_processed.jpg
    ip.save_processed_image("output_processed.jpg")
# проверяем, что скрипт запущен напрямую, а не импортирован как модуль
if __name__ == "__main__":
    main() # запускаем основную функцию main