user_num = int(input("Hello! Pleas enter tour number: "))
list_num = [9, 8, 4, 4, 3, 2]
search_num = list_num.count(user_num)

for elem in list_num:
    if search_num > 0:
        i = list_num.index(user_num)
        list_num.insert(i+search_num, user_num)
        break

    else:
        if user_num > elem:
            i = list_num.index(elem)
            list_num.insert(i, user_num)
            break

        elif user_num < list_num[len(list_num) - 1]:
            list_num.append(user_num)

print(list_num)