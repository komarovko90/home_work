class Road:
    _length = None
    _width = None

    def __init__(self, length, wid):
        self._length = length
        self._width = wid

    def mass_deter(self):
        '''
        расчет массы асфльта
        объем м3 * массу 1го квадратного метра асфальта 0.025тонн
        объем = ширина м * длина м * высота 0.05м
        :return: масса асфальта в тоннах
        '''
        return self._width * self._length * 0.05 * 0.025


try:
    width = int(input('Enter the width of the planned road in meters: '))
    length = int(input('Enter the length of the planned road in meters: '))
    if width >= 0 and length >= 0:
        rd = Road(length, width)
        print(f'{rd.mass_deter()} tons of asphalt will be required with a thickness of 5 cm.')
    else:
        print('Enter positive numbers')
except ValueError:
    print('Incorrect enter.')
