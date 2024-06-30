"""
В этом примере класс Worker не знает конкретной реализации задачи, которую он выполняет.
Вместо этого он зависит от абстракции Task.
Работник просто вызывает метод execute() объекта типа Task,
который он получает в качестве параметра конструктора.
Таким образом, он не привязан к конкретным классам PaintingTask или CodingTask,
что соответствует принципу инверсии зависимостей.
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
    def __init__(self, task: Task):
        self.task = task

    def perform_work(self):
        self.task.execute()
