user_ent = input("Hello! Pleas enter new lines:")
new_word = []
num = 1

for elem in range(user_ent.count(' ') + 1):
    new_word = user_ent.split()

    if len(str(new_word)) <= 10:
        print(f" {num} {new_word [elem]}")
        num += 1

    else:
        print(f" {num} {new_word [elem] [0:10]}")
        num += 1