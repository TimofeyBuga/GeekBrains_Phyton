sec = int(input("Введите время в секундах:"))
sec_lost = (sec % (3600 * 24)) % 60
minute = (sec // 60) % 60
hour = sec // 3600
answer_text = "Прошло времени в формате чч:мм:сс"


print("%s - %02d:%02d:%02d" % (answer_text, hour, minute, sec_lost))