# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу,
# открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

ang_rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_list = []

with open("task_4_file.txt") as f_obj:
    for line in f_obj:
        score = line.split(" - ")
        print(score)
        if score[0] in ang_rus:
             words = ang_rus[score[0]]
             new_list.append(f'{words} - {score[1]}')
    print(new_list)


with open("task_4_file_2.txt", "w", encoding="utf-8") as f_obj_2:
    f_obj_2.writelines(new_list)


# Можно ли таким образом решить данную задачу?
# Или это не будет считаться верным т.к. замена происходит не только "One", а "One - 1"
# Просто так в разы короче получается) Хоть и немного не честно))))

        # replace = {"One - 1": "Один - 1", "Two - 2": "Два - 2", "Three - 3": "Три - 3", "Four - 4": "Четыре - 4"}
        #
        # with open('task_4_file.txt') as f_in, open('task_4_file_2.txt', 'w', encoding="utf-8") as f_out:
        #     f_out.write('\n'.join([replace[key] for key in f_in.read().split('\n')]))