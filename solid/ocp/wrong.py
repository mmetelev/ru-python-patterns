class ImageViewer:
    def __init__(self):
        # Используемый формат изображения
        self.image_format = None

    # Метод для отображения изображения в выбранном формате
    def display_image(self, image):
        if self.image_format == "png":
            print("Отображение изображения в формате PNG")
        elif self.image_format == "jpeg":
            print("Отображение изображения в формате JPEG")
        elif self.image_format == "gif":
            print("Отображение изображения в формате GIF")
        else:
            print("Неподдерживаемый формат изображения")


# Пример использования
if __name__ == "__main__":
    image_viewer = ImageViewer()

    image_viewer.image_format = "png"
    image_viewer.display_image("image.png")

    image_viewer.image_format = "jpeg"
    image_viewer.display_image("image.jpeg")

    image_viewer.image_format = "gif"
    image_viewer.display_image("image.gif")

    # Новый формат добавляется путем добавления нового условия в метод display_image
    image_viewer.image_format = "bmp"
    image_viewer.display_image("image.bmp")
