my_str = input ('Введите произвольную строку: ')

#print (my_str)
my_list = my_str.split()

for num, el in enumerate(my_list, 1):
    print(f'{num}: {el[:10]}')