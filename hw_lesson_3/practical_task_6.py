# #Первый вариант

def big_let(a):
    return a.title()


print(big_let(input("enter word ")))


#Обыч вариант
def big_let_2(a):
    words = a.split()
    words_list = []

    for i in words:
        words_let = str(i)
        first_let = words_let[:1].upper()
        new_word = first_let + words_let[1:]
        words_list.append(new_word)
    return words_list


print(big_let_2(input("enter words ")))










