def my_div (arg1, arg2):
    try:
        result = arg1 / arg2
        return result
    except ZeroDivisionError:
        print ('Error - division by zero')

print('Function division')
try:
    val1 = float(input('Enter dividend: '))
    val2 = float(input('Enter divider: '))
    print('Result:', my_div(val1, val2))
except ValueError:
    print('Incorrect input')


