"""
В этом примере мы имеем классы для создания персонажей в игре.
Класс Character представляет собой продукт, который мы хотим создать.
Класс CharacterBuilder - это абстрактный строитель,
который определяет методы для установки различных характеристик персонажа.
Конкретные строители (WarriorBuilder и ArcherBuilder) реализуют методы
для установки конкретного оружия и брони для воина и лучника соответственно.
Директор CharacterDirector используется для управления процессом построения персонажа.

Применение:
* Паттерн Строитель полезен, когда у вас есть сложный объект,
который нужно создать с определенными шагами конструирования.

* Он помогает изолировать процесс конструирования объекта от его представления,
что делает код более гибким и легко расширяемым.

* Строители могут быть переиспользованы для создания различных вариаций объекта,
что способствует повторному использованию кода.
"""


# Продукт: персонаж
class Character:
    def __init__(self):
        self.name = None
        self.gender = None
        self.race = None
        self.weapon = None
        self.armor = None

    def display(self):
        print(
            f"Character: {self.name}, "
            f"Gender: {self.gender}, "
            f"Race: {self.race}, "
            f"Weapon: {self.weapon}, "
            f"Armor: {self.armor}"
        )


# Абстрактный строитель персонажа
class CharacterBuilder:
    def __init__(self):
        self.character = Character()

    def set_name(self, name):
        self.character.name = name

    def set_gender(self, gender):
        self.character.gender = gender

    def set_race(self, race):
        self.character.race = race

    def set_weapon(self, weapon):
        self.character.weapon = weapon

    def set_armor(self, armor):
        self.character.armor = armor

    def get_character(self):
        return self.character


# Конкретный строитель для создания персонажа-воина
class WarriorBuilder(CharacterBuilder):
    def set_weapon(self):
        self.character.weapon = "Sword"

    def set_armor(self):
        self.character.armor = "Plate"


# Конкретный строитель для создания персонажа-лучника
class ArcherBuilder(CharacterBuilder):
    def set_weapon(self):
        self.character.weapon = "Bow"

    def set_armor(self):
        self.character.armor = "Leather"


# Директор - управляет процессом построения персонажа
class CharacterDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_character(self, name, gender, race):
        self.builder.set_name(name)
        self.builder.set_gender(gender)
        self.builder.set_race(race)
        self.builder.set_weapon()
        self.builder.set_armor()

    def get_character(self):
        return self.builder.get_character()


# Пример использования паттерна Строитель
if __name__ == "__main__":
    # Создание строителя для персонажа-воина
    warrior_builder = WarriorBuilder()
    # Создание директора
    director = CharacterDirector(warrior_builder)
    # Создание персонажа-воина
    director.construct_character("Warrior", "Male", "Human")
    warrior = director.get_character()
    warrior.display()

    # Создание строителя для персонажа-лучника
    archer_builder = ArcherBuilder()
    # Создание директора
    director = CharacterDirector(archer_builder)
    # Создание персонажа-лучника
    director.construct_character("Archer", "Female", "Elf")
    archer = director.get_character()
    archer.display()
