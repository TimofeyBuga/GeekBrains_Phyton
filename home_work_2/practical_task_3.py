#Решение через dict:

month_num = int(input("Hello! Pleas enter month number from 1 to 12: "))

if month_num <= 12 and month_num >= 1:

    season_name = {1: 'Whinter', 2: 'Whinter', 3: 'Spring',  4: 'Spring',
                   5: 'Spring',  6: 'Summer',  7: 'Summer',  8: 'Summer',
                   9: 'Autumn',  10: 'Autumn', 11: 'Autumn', 12: 'Whinter'}

    season_name_dict = list(season_name.values())

    for num, name in enumerate(season_name_dict):

        if num == month_num-1:
            print(f"This month is season: {season_name_dict[num]}")


#Решения через list:

month_num = int(input("Hello! Pleas enter month number from 1 to 12: "))

season_name_list = ["Whinter", "Spring", "Summer", "Autumn"]

if month_num ==1 or month_num == 2 or month_num == 12:
    print(season_name_list[0])

elif month_num == 3 or month_num == 4 or month_num == 5:
    print(season_name_list[1])

elif month_num == 6 or month_num == 7 or month_num == 8:
    print(season_name_list[2])

elif month_num == 9 or month_num == 10 or month_num == 11:
    print(season_name_list[3])








