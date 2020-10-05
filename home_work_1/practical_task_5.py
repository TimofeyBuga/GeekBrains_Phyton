profit = int(input("Ввидите значение выручки:"))
cost = int(input("Ввидите значение издержек:"))
result_zero = "Ваш финансовый результат равен 0"
result_profit = profit - cost
result_cost = profit - cost

if profit > cost:
     print("Результа финансовой прибыли равен:", result_profit)
     worker_number = int(input("Ввидите число сотрудников вашей фирмы:"))
     worker_cash = result_profit / worker_number
     print("Прибыль фирмы в расчете на одного сотрудника равна:", worker_cash)
elif profit < cost:
     print("Результа финансового убытка равен:", result_cost)
else:
     print(result_zero)







