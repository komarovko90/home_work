import random

with open('numbers.txt', 'w', encoding='utf-8') as f:
    num_list = [str(random.randint(1, 100)) for _ in range(10)]
    f.write(' '.join(num_list))

with open('numbers.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    print(text)
    my_str = text.split()
    sum = 0
    for el in my_str:
        sum += int(el)
    print('Sum of numbers:', sum)

