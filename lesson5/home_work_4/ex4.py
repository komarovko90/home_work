new_str = []
with open('numbers.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
    dict_numbers = {
        1: 'Один',
        2: 'Два',
        3: 'Три',
        4: 'Четыре',
        5: 'Пять',
        6: 'Шесть',
        7: 'Семь'
    }
    for el in text:
        my_str = el.split()
        num = int(my_str[2])
        new_str.append(dict_numbers[num] + ' - ' + str(num) + '\n')

with open('new_numbers.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_str)
