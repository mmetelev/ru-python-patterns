"""
В этом примере HotBeverage - это абстрактный класс с шаблонным методом prepare(),
который определяет последовательность действий для приготовления горячего напитка.
Классы Coffee и Tea предоставляют конкретные реализации методов brew() и add_condiments(),
специфичных для каждого напитка.

Применение:

* Шаблонный метод используется, когда у вас есть алгоритм, который состоит из нескольких шагов,
и некоторые из этих шагов могут быть реализованы по-разному в подклассах.

* Этот паттерн помогает избежать дублирования кода и делает программу более гибкой,
позволяя подклассам переопределять определенные шаги алгоритма.
"""
from abc import ABC, abstractmethod


# Абстрактный класс для напитка
class HotBeverage(ABC):
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def boil_water(self):
        print("Кипятим воду")

    def pour_in_cup(self):
        print("Переливаем напиток в чашку")


# Конкретный класс для приготовления кофе
class Coffee(HotBeverage):
    def brew(self):
        print("Процесс заваривания кофе")

    def add_condiments(self):
        print("Добавляем сахар и молоко")


# Конкретный класс для приготовления чая
class Tea(HotBeverage):
    def brew(self):
        print("Процесс заваривания чая")

    def add_condiments(self):
        print("Добавляем лимон")


# Пример использования шаблона метода
if __name__ == "__main__":
    print("Готовим кофе:")
    coffee = Coffee()
    coffee.prepare()

    print("\nГотовим чай:")
    tea = Tea()
    tea.prepare()
