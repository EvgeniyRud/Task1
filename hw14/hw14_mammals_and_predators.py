from hw14_animal import Animal
from abc import ABC, abstractmethod

class Mammals(Animal):
    def __init__(self, name, age, kind_of_animal):
        super().__init__(name, age)
        self._kind_of_animal = kind_of_animal

    def make_noize(self):
        return 'I make noize - mammamls'

    @property  # Аналогичная функция получения защищенного параметра с помощью декоратора
    def kind_of_animal(self):  # в такую функцию из аргументов только self
        return self._kind_of_animal

    @kind_of_animal.setter
    def kind_of_animal(self, new_kind_of_animal):
        self._kind_of_animal = new_kind_of_animal


class Predator(Mammals):
    def __init__(self, name, age, _kind_of_animal, claw, beak):
        super().__init__(name, age, _kind_of_animal)
        self.claw = claw
        self.beak = beak

    @abstractmethod
    def tools_of_predator(self):
        pass

    def tools_of_predator(self):
        return f'I {self.claw} claws and also I {self.beak} beak'

    def make_noize(self):
        return 'I make noize'


if __name__ == '__main__':
    # barsik = Animal("Barsik", 2)
    # print(barsik.__str__())
    # print(barsik.make_noize())
    zebra = Mammals("Zebra", 4, "horse")
    print(zebra.__str__())
    print(zebra.kind_of_animal)
    zebra.kind_of_animal = "african_horse"
    print(zebra.kind_of_animal)
    tiger = Predator("Tiger", 3, "tiger", "have", "don`t have")
    print(tiger.__str__())
    print(tiger.tools_of_predator())
    print(tiger.kind_of_animal)
    tiger.kind_of_animal = "bengalian_tiger"
    print(tiger.kind_of_animal)

