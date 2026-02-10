import random


salary = int(input("Введите Вашу зарплату: "))
bonus = random.choice([True, False])
bonus_amount = random.randrange(1, 1000)

if bonus == True:
    new_salary = salary + bonus_amount
    print(f"{salary}, {bonus} - '${new_salary}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")
