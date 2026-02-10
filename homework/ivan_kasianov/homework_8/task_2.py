import sys
sys.set_int_max_str_digits(25000)


def progression():
    first_numb = 0
    second_numb = 1
    while True:
        yield first_numb
        sum_numb = first_numb + second_numb
        first_numb = second_numb
        second_numb = sum_numb


count = 1
for number in progression():
    if count == 5:
        print(number)
    elif count == 200:
        print(number)
    elif count == 1000:
        print(number)
    elif count == 100000:
        print(number)
        break
    count += 1
