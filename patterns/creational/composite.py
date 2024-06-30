"""
Паттерн Composite (Компоновщик) позволяет клиентам обрабатывать отдельные объекты
и их композиции единообразно.

В данном примере используется иерархия структуры документов,
где каждый документ может быть либо отдельным элементом (например, текстовым элементом),
либо контейнером для других элементов (например, абзацем с вложенными элементами).

Применение:

* Паттерн Composite полезен, когда вам нужно работать с иерархическими структурами объектов,
где каждый объект может быть либо отдельным элементом, либо контейнером для других элементов.

* Он позволяет клиентам обращаться к композиции объектов так же, как и к отдельным объектам,
что упрощает обработку сложных структур данных.

* Composite также позволяет добавлять и удалять элементы динамически,
что делает его гибким и подходящим для использования в различных сценариях.
"""

from abc import ABC, abstractmethod


class DocumentComponent(ABC):
    @abstractmethod
    def display(self):
        pass


class TextElement(DocumentComponent):
    def __init__(self, text):
        self.text = text

    def display(self):
        print(self.text)


class CompositeElement(DocumentComponent):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self):
        for child in self.children:
            child.display()


# Пример использования паттерна Composite
if __name__ == "__main__":
    main_document = CompositeElement()
    paragraph1 = CompositeElement()
    paragraph2 = CompositeElement()

    paragraph1.add(TextElement("Это первый параграф."))
    paragraph2.add(TextElement("Это второй параграф."))

    main_document.add(paragraph1)
    main_document.add(paragraph2)

    main_document.display()
