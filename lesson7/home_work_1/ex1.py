class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        my_str = ''
        for el in self.matrix:
            my_str += ' '.join(list(map(str, el))) + '\n'
        return my_str

    def __add__(self, other):
        '''
        Квадратная матрица
        '''
        my_matr = []
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            for i in range(len(self.matrix)):
                column = []
                for j in range(len(self.matrix[i])):
                    column.append(self.matrix[i][j] + other.matrix[i][j])
                my_matr.append(column)
            return Matrix(my_matr)
        else:
            print('Суммируются только матрицы одинаковых размерностей')


m1 = Matrix([[31, 22, 1, 1], [37, 43, 1, 1]])
m2 = Matrix([[31, 22, 2, 2], [37, 43, 2, 2]])
print(m1)
print(m2)
print(m1 + m2)
