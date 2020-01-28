class Cell:
    def __init__(self, count):
        self.count_cell = int(count)

    def __add__(self, other):
        return Cell(self.count_cell + other.count_cell)

    def __sub__(self, other):
        if self.count_cell - other.count_cell < 0:
            print('Отрицательное значение')
        else:
            return Cell(self.count_cell - other.count_cell)

    def __mul__(self, other):
        return Cell(self.count_cell * other.count_cell)

    def __truediv__(self, other):
        return Cell(self.count_cell // other.count_cell)

    def __str__(self):
        return f'Количество клеток - {self.count_cell}'

    def make_order(self, Cell, num):
        cnt_cell = Cell.count_cell
        while cnt_cell - num >= 0:
            print('* '*num)
            cnt_cell -= num
        print('* '*cnt_cell)


cl1 = Cell(50.5)
cl2 = Cell(5)
print(cl1 + cl2)
print(cl2 - cl1)
print(cl1 - cl2)
print(cl2 * cl1)
print(cl2 / cl1)
print(cl1 / cl2)
cl2.make_order(cl2, 4)
cl1.make_order(cl1, 9)