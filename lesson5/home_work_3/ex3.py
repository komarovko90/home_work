with open('workers.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
    f.seek(0)
    print(f.read())
    print('Employees whose salary are less than 20000:')
    average_sal = 0
    count_emp = 0
    for el in text:
        name, salary_str = el.split()
        salary = float(salary_str)
        average_sal += salary
        if salary < 20000:
            print(name, end=' ')
        count_emp += 1
    print(f'\nAverage salary of employees: {average_sal/count_emp:.2f}')
