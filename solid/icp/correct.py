class Worker:
    def work(self):
        pass

    def eat(self):
        pass


class Robot(Worker):
    def work(self):
        print("Робот выполняет работу")


class Human(Worker):
    def work(self):
        print("Человек выполняет работу")

    def eat(self):
        print("Человек обедает")
