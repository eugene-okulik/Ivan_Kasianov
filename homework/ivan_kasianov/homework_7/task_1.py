number = 25
while True:
    user_input = int(input("Введите число: "))
    if user_input == number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("попробуйте снова")
