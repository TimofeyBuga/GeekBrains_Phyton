# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

the_boys = {"Butcher": 40000, "Frenchie": 19000, "Mother's Milk": 30000, "The Female": 18000, "Hughie": 25000}

with open("task_3_file.txt", "w") as firm_the_boys:
    for name_worker, cash in the_boys.items():
        firm_the_boys.write(f"{name_worker} : {str(cash)}\n")


all_cash = 0
score = 0
workers = []
with open("task_3_file.txt", "r") as firm_the_boys:
    for line in firm_the_boys:
        print(line, end="")
        marks = line.split(":")
        if int(marks[1]) <= 20000:
            workers.append(marks[0])
        all_cash += int(marks[1])
        score += 1
counting_cash = all_cash / score

print(f"Workers: {workers}")
print(f"Average income: {counting_cash}")




