"""
Singleton (Одиночка)

Описание:

Паттерн Singleton является порождающим паттерном проектирования,
который гарантирует, что у класса есть только один экземпляр,
и предоставляет глобальную точку доступа к этому экземпляру.

Структура:

Singleton: Определяет статический метод get_instance(),
который возвращает единственный экземпляр класса.
Конструктор класса обычно объявляется как закрытый (private),
чтобы предотвратить создание экземпляров класса извне.

"""


class DatabaseConnection:
    _instance = None

    def __init__(self):
        # Здесь могут быть настройки соединения с базой данных
        self.connection = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def connect(self):
        # Логика соединения с базой данных
        print("Соединение с базой данных установлено")

    def disconnect(self):
        # Логика отключения от базы данных
        print("Соединение с базой данных разорвано")


# Использование паттерна Singleton
db_connection1 = DatabaseConnection.get_instance()
db_connection1.connect()

# Попытка создать еще один объект DatabaseConnection
db_connection2 = DatabaseConnection.get_instance()
db_connection2.connect()  # Это будет использовать то же самое соединение с базой данных, что и db_connection1

# Проверка, что db_connection1 и db_connection2 указывают на один и тот же объект
print(db_connection1 is db_connection2)  # Выведет True
