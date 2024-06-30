"""
В этом примере мы имеем класс Calculator, который выполняет операции над числами
с помощью различных стратегий (сложение, вычитание, умножение).
Стратегии инкапсулируют различные алгоритмы, которые могут быть применены к числам.

Применение:
* Паттерн Стратегия полезен, когда у вас есть семейство алгоритмов,
которые могут быть использованы в зависимости от контекста.

* Он помогает избежать дублирования кода и делает программу более гибкой и расширяемой.

* Стратегии могут быть легко добавлены или изменены без изменения контекста,
что делает паттерн очень удобным для использования в различных ситуациях.
"""
from abc import ABC, abstractmethod


# Абстрактный класс стратегии
class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, num1, num2):
        pass


# Конкретная стратегия: Сложение
class AdditionStrategy(OperationStrategy):
    def execute(self, num1, num2):
        return num1 + num2


# Конкретная стратегия: Вычитание
class SubtractionStrategy(OperationStrategy):
    def execute(self, num1, num2):
        return num1 - num2


# Конкретная стратегия: Умножение
class MultiplicationStrategy(OperationStrategy):
    def execute(self, num1, num2):
        return num1 * num2


# Класс контекста
class Calculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_operation(self, num1, num2):
        return self.strategy.execute(num1, num2)


# Пример использования паттерна Стратегия
if __name__ == "__main__":
    # Создание объектов стратегий
    addition = AdditionStrategy()
    subtraction = SubtractionStrategy()
    multiplication = MultiplicationStrategy()

    # Создание контекста с начальной стратегией (сложение)
    calculator = Calculator(addition)

    # Выполнение операций с разными стратегиями
    print("Сложение:", calculator.execute_operation(5, 3))
    calculator.set_strategy(subtraction)
    print("Вычитание:", calculator.execute_operation(5, 3))
    calculator.set_strategy(multiplication)
    print("Умножение:", calculator.execute_operation(5, 3))
