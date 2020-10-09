any_str = "Lighten up!"
any_int = 10
any_float = 45.14
any_list = ['a', '5']
any_tuple = ('b', '1')
any_dict = {'pizza': 'CHILL CHAN', 'burger': 'EGG DUMPTY'}
any_set = {"c", "d"}
any_bool = True

whole_register = [any_str, any_int, any_float, any_list, any_tuple, any_dict, any_set, any_bool]
print(f' All elements list: {whole_register}')
for elem in whole_register:

    print(f'This element: {elem} is {type(elem)}')


