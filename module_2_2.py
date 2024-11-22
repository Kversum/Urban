first = int(input('Ввеите первое число: '))
second = int(input('Ввеите второе число: '))
third = int(input('Ввеите третье число: '))
if first == second == third:
    print(3)
elif first != second != third:
    print(0)
elif first == second or first == third or second == first or second == third:
    print(2)
