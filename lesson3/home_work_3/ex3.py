def my_func2(val1, val2, val3):
    par = [val1, val2, val3]
    par.sort()
    return par[-1] + par[-2]

print(my_func2(-4, 7, 23))