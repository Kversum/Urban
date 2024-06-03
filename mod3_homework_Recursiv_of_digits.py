def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) == 1:
        return int(str_number) # Базовый случай: возвращаем цифру, если она одна
    else:
        first_digit = int(str_number[0])
    return first_digit * get_multiplied_digits(int(str_number[1:])) # Рекурсивный вызов

result = get_multiplied_digits(40203)
print((result))
