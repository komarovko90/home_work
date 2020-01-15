def int_func(text):
    my_list = text.split()
    for i in range(len(my_list)):
        my_list[i]=my_list[i].title()
    return ' '.join(my_list)

def int_func2(text):
    my_list = text.split()
    for i in range(len(my_list)):
        word = my_list[i]
        my_word = word[0].upper()
        for j in range(1, len(word)):
            my_word += word[j]
        my_list[i]=my_word
    return ' '.join(my_list)

str = input ('Введите слова, разделенные пробелом: ')
print(int_func(str))
print(int_func2(str))
# дополнительная строка 1