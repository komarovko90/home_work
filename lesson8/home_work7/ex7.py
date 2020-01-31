class Digit_complex:
    def __init__(self, x, y):
        self.num = complex(x, y)

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num

    def __str__(self):
        return self.num


complex1 = Digit_complex(1, 2)
complex2 = Digit_complex(3, 4)
print(complex1 + complex2)
print(complex1 * complex2)