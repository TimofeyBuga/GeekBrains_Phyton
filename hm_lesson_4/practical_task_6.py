from itertools import count
from itertools import cycle


def count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)


def cycle_func(my_list, iteration):
    i = 0
    iteration_numbers = cycle(my_list)
    while i < iteration:
        print(next(iteration_numbers))
        i += 1


count_func(start_number=int(input("enter start number: ")), stop_number=int(input("enter stop number: ")))
cycle_func(my_list=[1, 2], iteration=int(input("enter iteration: ")))