def get_multiplied_digits(number):
    str_number = str(number)
    first = str_number[0]
    for i in str_number[1:]:
        if int(i) > 0:
            temp = int(first) * (int(i))
            first = temp
    result = first
    return result


print(get_multiplied_digits(40203))
