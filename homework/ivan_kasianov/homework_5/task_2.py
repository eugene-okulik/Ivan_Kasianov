first_result = "результат операции: 42"
char_index_1 = first_result.index(":") + 2
print(int(first_result[char_index_1:]) + 10)

second_result = "результат операции: 514"
char_index_2 = second_result.index(":") + 2
print(int(second_result[char_index_2:]) + 10)

third_result = "результат работы программы: 9"
char_index_3 = third_result.index(":") + 2
print(int(third_result[char_index_3:]) + 10)
