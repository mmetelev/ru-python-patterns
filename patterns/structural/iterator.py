"""
Паттерн Итератор позволяет последовательно перебирать элементы коллекции
без раскрытия её внутренней структуры.
В данном примере StudentGroup представляет собой коллекцию студентов,
а StudentIterator - итератор для перебора этих студентов.

Применение:
* Паттерн Итератор полезен, когда у вас есть коллекция объектов,
и вы хотите предоставить стандартный способ перебора их элементов.

* Он позволяет абстрагироваться от внутренней структуры коллекции и
предоставляет клиентам удобный интерфейс для перебора элементов.

* Итераторы также могут быть реализованы с различными поведениями,
такими как обход в глубину или в ширину, фильтрация элементов и т. д.,
что делает паттерн гибким и мощным для использования.
"""
from collections.abc import Iterator, Iterable


# Класс, представляющий студента
class Student:
    def __init__(self, name):
        self.name = name


# Класс, представляющий группу студентов
class StudentGroup(Iterable):
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __iter__(self):
        return StudentIterator(self.students)


# Класс итератора для студентов
class StudentIterator(Iterator):
    def __init__(self, students):
        self.students = students
        self.index = 0

    def __next__(self):
        if self.index < len(self.students):
            student = self.students[self.index]
            self.index += 1
            return student
        else:
            raise StopIteration


# Пример использования паттерна Итератор
if __name__ == "__main__":
    group = StudentGroup()
    group.add_student(Student("Иванов"))
    group.add_student(Student("Петров"))
    group.add_student(Student("Сидоров"))

    # Использование итератора для перебора студентов в группе
    iterator = iter(group)
    for student in iterator:
        print(student.name)
