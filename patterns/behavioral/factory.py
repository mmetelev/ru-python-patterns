"""
Factory (Фабрика)

Описание:

Паттерн Factory (Фабрика) является порождающим паттерном проектирования,
который предоставляет интерфейс для создания объектов с определенными параметрами.
Фабрика делегирует создание объектов своим подклассам, которые реализуют конкретную логику создания объектов.

Структура:

- Product (Продукт): Определяет интерфейс создаваемых объектов.
- ConcreteProduct (Конкретный продукт): Реализует интерфейс Product.
- Factory (Фабрика): Определяет метод create_vehicle(), который создает объекты Product.
  Этот метод может иметь различные реализации в подклассах фабрики.
- ConcreteFactory (Конкретная фабрика): Реализует метод create_vehicle() для создания конкретных продуктов.
"""


class Vehicle:
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("Автомобиль едет по дороге")


class Plane(Vehicle):
    def move(self):
        print("Самолет летит в небе")


class Ship(Vehicle):
    def move(self):
        print("Корабль плывет по воде")


class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "plane":
            return Plane()
        elif vehicle_type == "ship":
            return Ship()
        else:
            raise ValueError("Неверный тип транспортного средства")


# Использование фабрики для создания транспортных средств
car = VehicleFactory.create_vehicle("car")
car.move()  # Выведет: "Автомобиль едет по дороге"

plane = VehicleFactory.create_vehicle("plane")
plane.move()  # Выведет: "Самолет летит в небе"

ship = VehicleFactory.create_vehicle("ship")
ship.move()  # Выведет: "Корабль плывет по воде"
