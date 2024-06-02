from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Hello. My name is {self.name}. I am {self.age} year(s) old'

    @abstractmethod
    def make_noize(self):
        return 'I make noize'

    def make_noize(self):
        return 'I make noize'


if __name__ == '__main__':
    maximus = Animal("Maximus", 2)
    print(maximus.__str__())
    print(maximus.make_noize())



