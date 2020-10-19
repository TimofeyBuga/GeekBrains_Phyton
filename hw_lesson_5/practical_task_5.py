# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open("task_5_file.txt", "w") as f_obj:
    line = input("Enter your numbers \n")
    f_obj.writelines(line)
    numbers = line.split()

    print(sum(map(int, numbers)))


