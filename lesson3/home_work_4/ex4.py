def my_func (x, y):
    if y >= 0:
        return 'Некорректно введена степень числа'
    return x**y


def my_func2 (x, y):
    if y >= 0:
        return 'Некорректно введена степень числа'
    y = abs(y)
    res = x
    for i in range(1, y):
        res *= x
    return 1/res

try:
    number = float(input('Введите число: '))
    power = int(input('Введите степень числа (целое отрицательное): '))
    print(my_func(number, power))
    print(my_func2(number, power))
except ValueError:
    print ('Некорректный ввод')