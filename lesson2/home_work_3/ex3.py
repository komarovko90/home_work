while True:
    str_month = input ('Введите номер месяца (1..12): ')
    try:
        num_month = int(str_month)
    except ValueError:
        print('Некорректный ввод')
        continue
    if num_month < 1 or num_month > 12:
        print('Введите в диапазоне от 1 до 12.')
    else:
        break

seasons_lst = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

for i in range(len(seasons_lst)):
    if num_month in seasons_lst[i]:
        if i == 0:
            print ('Зима')
        elif i == 1:
            print('Весна')
        elif i == 2:
            print('Лето')
        else:
            print('Осень')
        break

seasons_name = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dct = dict(zip(seasons_name, seasons_lst))
for key, value in seasons_dct.items():
    if num_month in value:
        print (key)

