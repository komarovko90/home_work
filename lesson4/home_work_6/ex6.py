import sys
from itertools import count, cycle

def func(arg1, arg2):
    try:
        num = float(arg1)
        for i in count(num):
            if i > num + 10:
                break
            print(i)
    except ValueError:
        print('Incorrect first argument')

    j = 0
    for el in cycle(arg2):
        if j >= 10:
            break
        print(el)
        j+=1


try:
    func(sys.argv[1], sys.argv[2])
except IndexError:
    print('Missing data')

