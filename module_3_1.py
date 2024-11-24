calls = 0
def count_calls():  # Подсчитывает вызовы остальных функций
    global calls
    calls += 1
def string_info(stroka):
    count_calls()
    # принимает аргумент - строку и возвращает кортеж из длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    kortej = (len(stroka), stroka.upper(), stroka.lower())
    return kortej

def is_contains(string, list_to_search):
    count_calls()
    # Принимает два аргумента: строку и список. Возвращает True, если строка находится в списке, иначе False.
    string_l = string.lower()
    for n in list_to_search:
        if string_l == n.lower():
            match = True
            break
        else:
            match = False
    return (match)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print('Кол-во вызовов функций:', calls)
