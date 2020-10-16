list_numbers = [10, 8, 27, 8, 15, 9, 84, 34, 9, 46, 58, 5, 100]
new_list = [el for el in list_numbers if el > list_numbers[list_numbers.index(el)-1]]


print(new_list)