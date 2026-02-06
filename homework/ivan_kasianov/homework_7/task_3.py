first_result = "результат операции: 42"
second_result = "результат операции: 54"
third_result = "результат работы программы: 209"
fourth_result = "результат: 2"


def program_result(i):
    # Сначала хотел не объявлять переменную "b" и сразу всё закинуть в print, но потом решил,
    # что строк кода станет меньше,но читабельность ухудшится и решил оставить переменную
    b = i.index(":") + 2
    print(int(i[b:]) + 10)


program_result(first_result)
program_result(second_result)
program_result(third_result)
program_result(fourth_result)
