class Bird:
    def fly(self):
        pass


class Ostrich(Bird):
    def fly(self):
        # Нарушение принципа LSP: страусы не могут летать
        print("Страусы не могут летать")


def make_bird_fly(bird):
    bird.fly()


# Создаем экземпляры классов Bird и Ostrich
bird = Bird()
ostrich = Ostrich()

# Вызываем функцию с экземплярами
make_bird_fly(bird)
make_bird_fly(ostrich)
