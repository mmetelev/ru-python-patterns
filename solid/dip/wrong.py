"""
В этом примере класс Worker прямо создает экземпляр класса PaintingTask внутри
своего метода perform_work(). Это нарушение принципа инверсии зависимостей,
потому что Worker теперь привязан к конкретной реализации задачи PaintingTask,
что делает его менее гибким для изменений и усложняет его тестирование.
"""


class Task:
    def execute(self):
        pass


class PaintingTask(Task):
    def execute(self):
        print("Работник рисует картину")


class CodingTask(Task):
    def execute(self):
        print("Работник пишет код")


class Worker:
    def perform_work(self):
        task = PaintingTask()
        task.execute()
