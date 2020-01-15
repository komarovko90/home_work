my_list = [7, 5, 3, 3, 2]
print('Текущий рейтинг: ', my_list)

while True:
    str_num = input ('Введите натуральное число (команда "stop" для окончания ввода): ')
    if str_num == 'stop':
        break
    try:
        number = float(str_num)
    except ValueError:
        print('Некорректный ввод')
        continue

    if number > 0:
        # основной код
        for i in range(len(my_list)):
            if number > my_list[i]:
                my_list.insert(i, number)
                print(my_list)
                break
            elif i + 1 == len(my_list):
                my_list.append(number)
                print(my_list)
    else:
        print('Введено не натуральное число!')
