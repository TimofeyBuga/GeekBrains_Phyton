#Первый вариант — возведение в степень с помощью оператора **

def my_func(x, y):
    return x ** y


print(my_func(int(input("Enter first number ")), int(input("Enter second number "))))


#Второй вариант - предусматривающий использование цикла.

def my_func_2(x, y):
    ext = 1

    for i in range(y):
        ext = ext * x
    return ext


print(my_func(int(input("enter first number ")), int(input("enter second number "))))