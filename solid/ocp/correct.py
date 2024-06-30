from abc import ABC, abstractmethod


# Базовый класс для всех форматов изображений
class ImageFormat(ABC):
    @abstractmethod
    def display(self, image):
        pass


# Класс для отображения изображений в формате PNG
class PNGFormat(ImageFormat):
    def display(self, image):
        print("Отображение изображения в формате PNG")


# Класс для отображения изображений в формате JPEG
class JPEGFormat(ImageFormat):
    def display(self, image):
        print("Отображение изображения в формате JPEG")


# Класс для отображения изображений в формате GIF
class GIFFormat(ImageFormat):
    def display(self, image):
        print("Отображение изображения в формате GIF")


# Допустим, вы хотите добавить поддержку формата BMP в будущем
# Создадим новый класс для отображения изображений в формате BMP, не изменяя существующий код
class BMPFormat(ImageFormat):
    def display(self, image):
        print("Отображение изображения в формате BMP")


# Класс приложения для отображения изображений
class ImageViewer:
    def __init__(self):
        # Используемый формат изображения
        self.image_format = None

    # Метод для отображения изображения в выбранном формате
    def display_image(self, image):
        self.image_format.display(image)


# Пример использования
if __name__ == "__main__":
    image_viewer = ImageViewer()

    # Переключаемся между различными форматами изображений без изменения кода класса ImageViewer
    image_viewer.image_format = PNGFormat()
    image_viewer.display_image("image.png")

    image_viewer.image_format = JPEGFormat()
    image_viewer.display_image("image.jpeg")

    image_viewer.image_format = GIFFormat()
    image_viewer.display_image("image.gif")

    # Добавляем поддержку нового формата без изменения существующего кода
    image_viewer.image_format = BMPFormat()
    image_viewer.display_image("image.bmp")
