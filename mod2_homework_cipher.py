n = int(input('Введите число: '))
pas = []
for i1 in range(1, 21):
    for i2 in range(1, 21):
        res = i1 + i2
        if n % res == 0 and i1 != i2:
            if pas.count(i1 and i2):
                continue
            else:
                pas.append(i1)
                pas.append(i2)
print(*pas)
