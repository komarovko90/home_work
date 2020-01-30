from abc import ABC, abstractmethod


class Clothes:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def __add__(self, other):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v
        self.cloth = self.v/6.5 + 0.5

    def __add__(self, other):
        return self.cloth + other.cloth

    def __str__(self):
        return f'Ткани {self.cloth:.2f} необходимо для пошива {self.name}'

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v < 30:
            self.__v = 30
        elif v > 60:
            self.__v = 60
        else:
            self.__v = v

class Costume(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h
        self.cloth = self.h * 2 + 0.3

    def __add__(self, other):
        return self.cloth + other.cloth

    def __str__(self):
        return f'Ткани {self.cloth:.2f} необходимо для пошива {self.name}'

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h < 1.2:
            self.__h = 1.2
        elif h > 2.2:
            self.__h = 2.2
        else:
            self.__h = h


coat1 = Coat('Black coat', 65)
costume1 = Costume('Brioni', 1)
print(coat1)
print(costume1)
print(coat1.cloth)
print(costume1.cloth)
print(f'Количество ткани потребуется для {coat1.name} и {costume1.name}: {coat1 + costume1}')
print(f'Количество ткани потребуется для {costume1.name} и {coat1.name}: {costume1 + coat1}')