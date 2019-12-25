start_dist = int(input('Введите текущую дистанцию [km]: '))
finish_dist = int(input('Введите желаемую дистанцию [km]: '))

current_dist = start_dist
day = 1
print (f'{day}-й день: {current_dist:.2f}')
while current_dist < finish_dist:
    day += 1
    current_dist *= 1.1
    print (f'{day}-й день: {current_dist:.2f}')

print (f'На {day}-й день спортсмен достиг результата - не менее {finish_dist} км ')