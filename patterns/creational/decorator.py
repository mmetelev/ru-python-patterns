"""
Паттерн Декоратор позволяет динамически добавлять новую функциональность объектам,
не изменяя их исходного кода. В данном примере используется кофейня,
где можно заказать различные напитки с добавлением различных опций (молоко, шоколад, взбитые сливки).

Применение:

* Паттерн Декоратор полезен, когда вам нужно добавить новую функциональность к объекту
без изменения его исходного кода.

* Он позволяет расширять функциональность объекта динамически,
а также комбинировать различные декораторы для получения различных вариаций объекта.

* Декоратор также делает код более гибким и модульным,
поскольку позволяет выделить различные аспекты функциональности в отдельные классы.

"""
from abc import ABC, abstractmethod


# Абстрактный класс напитка
class Beverage(ABC):
    @abstractmethod
    def cost(self):
        pass


# Конкретный класс напитка: Эспрессо
class Espresso(Beverage):
    def cost(self):
        return 1.50


# Декоратор: Добавляет молоко к напитку
class MilkDecorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + 0.50


# Декоратор: Добавляет шоколад к напитку
class ChocolateDecorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + 0.75


# Декоратор: Добавляет взбитые сливки к напитку
class WhippedCreamDecorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + 0.60


# Пример использования паттерна Декоратор
if __name__ == "__main__":
    espresso = Espresso()
    print("Цена за эспрессо:", espresso.cost())

    latte = MilkDecorator(espresso)
    print("Цена за латте:", latte.cost())

    mocha = ChocolateDecorator(WhippedCreamDecorator(latte))
    print("Цена за мокко:", mocha.cost())
