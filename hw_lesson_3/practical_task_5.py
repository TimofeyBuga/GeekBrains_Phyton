def sum_num():
    sum_res = 0
    str_num = False

    while str_num == False:
        number = input('pleas input your numbers or Q for escape - ').split()
        res = 0

        for num in range(len(number)):
            if number[num].upper() == 'Q':
                str_num = True
                break
            else:
                res = res + int(number[num])
        sum_res = sum_res + res

        print(f'Your current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')


sum_num()