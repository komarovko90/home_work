class OwnError(Exception):
    def __init__(self, txt):
        self.text = txt


print('Function division')
while True:
    in_str_1 = input('Enter dividend (or q for quit): ')
    if in_str_1 == 'q':
        break
    in_str_2 = input('Enter divider: ')
    try:
        in_str_1 = float(in_str_1)
        in_str_2 = float(in_str_2)
        if in_str_2 == 0:
            raise OwnError('Error: division by zero!!')
    except ValueError:
        print('Incorrect input')
    except OwnError as err:
        print(err)
    else:
        print('Result:', in_str_1 / in_str_2)

