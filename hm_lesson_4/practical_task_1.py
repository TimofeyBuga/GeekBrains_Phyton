from sys import argv

script_name, worked_time, cash, prem_cash = argv

salary = int(worked_time) * int(cash) + int(prem_cash)


print(f"Your pay is equal {salary}")
