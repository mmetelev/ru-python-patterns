"""
Паттерн Команда позволяет инкапсулировать запрос в виде объекта,
что позволяет параметризовать клиентов с различными запросами,
очередями или журналами запросов, а также поддерживать отмену операций.

Применение:
* Паттерн Команда полезен, когда вам нужно параметризовать объекты с различными операциями,
выполняемыми в ответ на запросы.

* Он позволяет создавать системы, где клиенты могут инкапсулировать операции в отдельные объекты,
что делает их более гибкими и расширяемыми.

* Команды также могут быть использованы для реализации отмены операций (откат изменений)
или выполнения операций в различных контекстах.
"""

from abc import ABC, abstractmethod


# Абстрактный класс команды
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Конкретная команда: Включить свет
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


# Конкретная команда: Выключить свет
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


# Класс-получатель: Свет
class Light:
    def turn_on(self):
        print("Свет включен")

    def turn_off(self):
        print("Свет выключен")


# Класс инициатор: Пульт управления
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()


# Пример использования паттерна Команда
if __name__ == "__main__":
    light = Light()
    light_on_command = LightOnCommand(light)
    light_off_command = LightOffCommand(light)

    remote_control = RemoteControl()

    remote_control.set_command(light_on_command)
    remote_control.press_button()

    remote_control.set_command(light_off_command)
    remote_control.press_button()
