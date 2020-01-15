def sum_number(my_list):
    global result
    for el in my_list:
        if el == '*':
            print(f'Сумма чисел равна: {result}')
            return True
        try:
            number = float(el)
        except ValueError:
            print('Некорректный ввод')
            return True
        result += number

result = 0.0
while True:
    str = input ('Введите числа, разделенные пробелом (* - конец ввода): ')
    my_list = str.split()
    if sum_number(my_list):
        break