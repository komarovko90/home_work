goods = []
item = {
    'название': None,
    'цена': None,
    'количество': None,
    'ед': None
    }
i = 1
question = None
while question != 'нет':
    item['название'] = input ('Введите наименование товара: ')
    #ввод и проверка стоимости
    while True:
        try:
            cost = int (input('Введите стоимость товара: '))
            if cost < 0:
                print('Ошибка: отрицательное значение')
                continue
            item['цена'] = cost
            break
        except ValueError:
            print('Некорректный ввод')
    #ввод и проверка количества
    while True:
        try:
            number = int(input('Введите количество товара: '))
            if number <= 0:
                print('Ошибка: некорректное количество товара')
                continue
            item['количество'] = number
            break
        except ValueError:
            print('Некорректный ввод')
    item['ед'] = input('Введите единицу измерения товара: ')
    goods.append((i, item.copy()))
    # печать товаров
    print('Итого товаров:')
    print(type(goods))
    for el in goods:
        print(el)
    i += 1
    # запрос на ввод доп позиции
    while True:
        question = input('Хотите добавить еще позицию? (да/нет): ')
        if question == 'да' or question == 'нет':
            print('-' * 50)
            break
        else:
            print('Некорректный ввод!')

# анализ полученных данных
my_list_name = []
my_list_cost = []
my_list_num = []
my_list_unit = []
for el in goods:
    my_list_name.append(el[1]['название'])
    my_list_cost.append(el[1]['цена'])
    my_list_num.append(el[1]['количество'])
    if el[1]['ед'] not in my_list_unit:
        my_list_unit.append(el[1]['ед'])

result = dict()
result['название'] = my_list_name
result['цена'] = my_list_cost
result['количество'] = my_list_num
result['ед'] = my_list_unit
print('-' * 50)
print('Анализ данных:')
print (type(result))
for key, value in result.items():
    print(key, value)
