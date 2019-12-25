revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))

if revenue > costs:
    print ('Фирма приносит доход!')
    profitability = (revenue - costs) / revenue * 100
    print (f'Рентабельность составила {int(profitability)}%')
    employee = int(input('Введите количество сотрудников фирмы: '))
    profit = (revenue - costs) / employee
    print (f'Прибыль в расчете на одного сотрудника: {profit:.2f}')
elif revenue < costs:
    print('Фирма несет убытки!')
else:
    print('Фирма вышла в 0!')
