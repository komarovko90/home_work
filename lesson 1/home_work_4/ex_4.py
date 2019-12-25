numbers = int(input('Enter an integer: '))

k=1
max_num = 0

while numbers // k != 0:
    num = numbers % (k * 10)
    num //= k
    if num == 9:
        print (f'{num} maximum digit')
        break
    elif num > max_num:
        max_num = num
    k *= 10
else:
    print(f'{max_num} maximum digit')








