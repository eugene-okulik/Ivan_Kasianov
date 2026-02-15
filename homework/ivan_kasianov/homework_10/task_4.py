PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_price_list = PRICE_LIST.split('\n')
new_price_list2 = [tuple(i.split(" ")) for i in new_price_list]
new_dict = {key: int(value.strip("р")) for key, value in new_price_list2}


print(new_dict)
