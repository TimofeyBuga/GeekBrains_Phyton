# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные,
# вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


new_file_text = []

while True:
    data_text = input("Write your text\n")
    if data_text == "":
        print(new_file_text)
        exit()
    else:
        newline = data_text
        new_file_text.append(newline)

    with open("task_1_file.txt", "w") as f_new:
        f_new.writelines(new_file_text)


