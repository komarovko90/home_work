num = input('Enter an integer: ')

num_2 = f'{num}{num}'
num_3 = f'{num_2}{num}'
print(num)
print(num_2)
print(num_3)
print(f'{num} + {num_2} + {num_3} = {int(num) + int(num_2) + int(num_3)}')