with open('disciplines.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
    discipline = {}
    for el in text:
        my_str = el.split()
        sum = 0
        for i in range(1, len(my_str)):
            if my_str[i] != '-':
                sum += int(my_str[i][:my_str[i].find('(')])
        discipline[my_str[0][:-1]] = sum
    print(discipline)
