def get_multiplied_digits(number):
    if number == 0:
        number = 1
    str_number = str(number)
    if len(str_number) == 1:
        return int(str_number)
    else:
        first_digit = int(str_number[0])
    return first_digit * get_multiplied_digits(int(str_number[1:]))


print(get_multiplied_digits(40203))
print(get_multiplied_digits(402030))
print(get_multiplied_digits(40))