def func_division(a, b):
    try:
        c = a / b
        return c
    except ValueError:
        return print("Pleas enter only number.")
    except ZeroDivisionError:
        return print("Attention! can't use zero")


print(func_division(int(input("Enter first number ")), int(input("Enter second number "))))




