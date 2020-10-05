numbers = int(input("Введите целое пложительное число:"))
number_max = numbers%10
numbers = numbers//10

while numbers > 0:
    if numbers%10 > number_max:
        number_max = numbers%10
    numbers = numbers//10
print("Самая большая цифра в данном числе:", number_max)