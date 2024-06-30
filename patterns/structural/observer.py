"""
Паттерн Наблюдатель (или Издатель-Подписчик) позволяет объектам оповещать
другие объекты об изменениях своего состояния.

В данном примере Weather является наблюдаемым объектом,
а WeatherDisplay - наблюдателем, который отображает текущую погоду на экране.

Применение:
* Паттерн Наблюдатель полезен, когда у вас есть объекты,
которые должны быть оповещены об изменениях в других объектах.

* Он позволяет реализовать слабую связь между наблюдаемыми и наблюдателями,
что делает систему более гибкой и расширяемой.

* Наблюдатели также могут быть добавлены и удалены динамически,
что делает паттерн подходящим для использования в различных сценариях,
таких как обработка событий, уведомления и реакция на изменения состояния объектов.
"""


# Абстрактный класс Наблюдаемого объекта
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, data):
        for observer in self.observers:
            observer.update(data)


# Абстрактный класс Наблюдателя
class Observer:
    def update(self, data):
        pass


# Конкретный класс Наблюдаемого объекта: Погода
class Weather(Subject):
    def set_weather(self, weather_data):
        self.notify(weather_data)


# Конкретный класс Наблюдателя: Отображение погоды на экране
class WeatherDisplay(Observer):
    def update(self, data):
        print("Погода на сегодня:", data)


# Пример использования паттерна Наблюдатель
if __name__ == "__main__":
    weather = Weather()
    display1 = WeatherDisplay()
    display2 = WeatherDisplay()

    weather.attach(display1)
    weather.attach(display2)

    weather.set_weather("Солнечно")
