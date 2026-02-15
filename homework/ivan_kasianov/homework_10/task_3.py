def new_calc(func):

    def wrapper(*args):
        new_args = list(args)
        if new_args[0] < 0 or new_args[1] < 0:
            new_args[2] = "*"
            result = func(*new_args)
            return result
        elif new_args[0] == new_args[1]:
            new_args[2] = "+"
            result = func(*new_args)
            return result
        elif new_args[0] > new_args[1]:
            new_args[2] = "-"
            result = func(*new_args)
            return result
        elif new_args[0] < new_args[1]:
            new_args[2] = "/"
            result = func(*new_args)
            return result
    return wrapper


first = int(input("Введите превое число: "))
second = int(input("Введите второе число: "))


@new_calc
def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "/":
        return first / second
    elif operation == "*":
        return first * second


print(calc(first, second, "+"))
