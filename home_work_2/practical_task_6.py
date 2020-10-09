new_product = int(input("Hello! Pleas enter number product: "))
max_product = 1
new_dict = []
new_list = []
analys_product = {}

while max_product <= new_product:
    new_dict = dict({'Name product': input("Enter name product: "), 'Price': input("Enter price product: "),
                    'Quantiy': input('Enter quantiy product: '), 'Units': input("Enter units product ")})
    new_list.append((max_product, new_dict))
    max_product += 1
    analys_product = dict({'Name product': new_dict.get('Name product'), 'Price': new_dict.get('Price'),
                'Quantiy': new_dict.get('Quantiy'), 'Units': new_dict.get('Units')})

print(new_list)
print(analys_product)


