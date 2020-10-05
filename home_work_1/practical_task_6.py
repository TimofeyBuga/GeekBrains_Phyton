first_result = int(input("Результат первого дня в км.:"))
final_result = int(input("Общий резултат спортсмена в км.:"))
result_up = (first_result / 100) * 10
chek_day = 0

while first_result < final_result:
    first_result = first_result + result_up
    chek_day = chek_day + 1
print("На", chek_day , "день. Спортсмен достигнет результата не мнее", final_result, "км")