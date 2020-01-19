def fact(num):
    my_list = [el for el in range(1, num+1)]
    for el in my_list:
        yield el


number = 10
print(f'Factorial number - {number}!:')
my_str = ''
result = 1
for el in fact(number):
    result *= el
    my_str = my_str + str(el) + '*'
print(my_str[:-1], '=', result)
