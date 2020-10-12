def my_func(a, b, c):
    number_list = [a, b, c]
    number_min = min(number_list)
    number_list.remove(number_min)
    print(sum(number_list))


my_func(int(input("Enter first number ")), int(input("Enter second number ")), int(input("Enter third number ")))
