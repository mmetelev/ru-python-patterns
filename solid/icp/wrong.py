class Worker:
    def work(self):
        pass


class Robot(Worker):
    def work(self):
        print("Робот выполняет работу")

    def eat(self):
        pass  # Робот не может есть, этот интерфейс не нужен


class Human(Worker):
    def work(self):
        print("Человек выполняет работу")

    def eat(self):
        print("Человек обедает")
