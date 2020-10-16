from functools import reduce


def my_func(el_p, el):
    return el_p * el


even_numbers = [el for el in range(100, 1001) if el % 2 == 0]
multi_numbers = reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0])


print(even_numbers)
print(multi_numbers)
