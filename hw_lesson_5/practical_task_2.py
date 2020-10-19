# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.


my_list = ['Black\n', 'White\n', 'Gray\n']

with open("task_2_file.txt", 'w') as f_new:
    f_new.writelines(my_list)

with open("task_2_file.txt") as f_new:
    score_lines = 0
    score_letters = 0
    for lines in f_new:
        score_lines += lines.count("\n")
        score_letters = len(lines)-1
        print(f"The score of letters in this line is {score_letters}")
    print(f"Score of lines {score_lines}")