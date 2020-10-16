list_numbers = [10, 10, 5, 4, 1, 18, 18, 10, 8, 19, 19, 59, 8]
new_list = [el for el in list_numbers if list_numbers.count(el) < 2]


print(new_list)