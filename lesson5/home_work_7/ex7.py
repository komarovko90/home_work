import json

finish_list = []
with open('company.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
    average_profit = 0
    count_comp = 0
    dict_company = {}
    for el in text:
        my_str = el.split()
        revenue = int(my_str[2])
        cost = int(my_str[3])
        profit = revenue - cost
        if profit > 0:
            average_profit += profit
            count_comp += 1
        dict_company[my_str[0]] = profit
    average_profit = average_profit/count_comp
    finish_list = [dict_company, {'average_profit': average_profit}]

with open('result.json', 'w') as f:
    json.dump(finish_list, f, indent=4)
