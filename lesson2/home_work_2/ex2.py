print ('Введите элементы списка (для окончания ввода используйте команду "stop").')
my_list = []
my_str = ''
i = 1
while True:
    my_str = input(f'Введите {i} элемент (или "stop"): ')
    if my_str == 'stop':
        break
    my_list.append(my_str)
    i += 1

print (my_list)
i = 1
while i < len(my_list):
    el = my_list[i]
    my_list[i] = my_list[i-1]
    my_list[i-1] = el
    i += 2
print (my_list)
