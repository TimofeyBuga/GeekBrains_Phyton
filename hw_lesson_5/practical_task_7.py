# 7. Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл,
# вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]


import json
income = {}
inc = {}
inc_score = 0
income_aver = 0
i = 0
with open("task_7_file.txt") as file:
    for line in file:
        name_firm, own, earnings, damages = line.split()
        income[name_firm] = int(earnings) - int(damages)
        if income.setdefault(name_firm) >= 0:
            inc_score = inc_score + income.setdefault(name_firm)
            i += 1
    if i >= 0:
        income_aver = inc_score / i
        print(f"Average profit: {income_aver}")
    else:
        print(f"Not average profit")
    inc = {"Average profit": round(income_aver)}
    income.update(inc)
    print(f'Profit for each company: {income}')

with open("task_7_file.json", "w") as write_js:
    json.dump(income, write_js)

    js_str = json.dumps(income)
    print(f"JSON file created: {js_str}")
