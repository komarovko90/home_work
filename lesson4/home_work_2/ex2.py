import random

my_list = []
for _ in range(10):
    my_list.append(random.randint(0, 500))
print(my_list)

new_list = [my_list[i] for i in range(1, len(my_list)-1) if my_list[i] > my_list[i-1]]
print(new_list)