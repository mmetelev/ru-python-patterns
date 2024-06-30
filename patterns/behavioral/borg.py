"""
В этом примере класс Borg реализует паттерн Borg (Моносостояние),
обеспечивая разделяемое состояние между всеми экземплярами.
Класс Logger является подклассом Borg и использует разделяемое состояние для хранения логов.
При добавлении сообщений в один логгер, они будут доступны и в другом логгере,
так как они разделяют общее состояние.

Применение:
* Паттерн Borg полезен, когда нужно создать группу объектов, которые разделяют общее состояние.
* Он может быть использован для реализации пула ресурсов, где все объекты пула используют общие ресурсы.
* Borg также может быть полезен для создания группы конфигурационных объектов,
где изменения в одном объекте автоматически отражаются во всех остальных объектах.
"""


class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state


class Logger(Borg):
    def __init__(self, name):
        Borg.__init__(self)
        self.name = name
        self.log = []

    def log_message(self, message):
        self.log.append(message)

    def display_log(self):
        print(f"Log for {self.name}:")
        for message in self.log:
            print(message)


# Пример использования паттерна Borg для создания группы логгеров
if __name__ == "__main__":
    logger1 = Logger("Logger 1")
    logger2 = Logger("Logger 2")

    logger1.log_message("Error: File not found")
    logger2.log_message("Warning: Memory running low")

    # Оба логгера имеют доступ к одному и тому же состоянию
    logger1.display_log()
    logger2.display_log()
