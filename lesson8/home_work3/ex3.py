class OwnError(Exception):
    def __init__(self, txt):
        self.text = txt


in_str_1 = input('Enter integer (or q for quit): ')
list_digit = []
while in_str_1 != 'q':
    try:
        if not in_str_1.isdigit():
            raise OwnError('Error: not digit!')
    except OwnError as err:
        print(err)
    else:
        list_digit.append(int(in_str_1))
    finally:
        in_str_1 = input('Enter integer (or q for quit): ')
print(list_digit)