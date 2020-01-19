import random

my_list = []
for _ in range(5):
    my_list.append(random.randint(10, 15))
print(my_list)

new_list = [el for el in my_list if my_list.count(el) < 2]
print(new_list)
