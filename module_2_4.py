numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(2, len(numbers)+1):
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
    if is_prime == True:
        primes.append(i)
    else:
        not_primes.append(i)
        is_prime = True
print('Простые числа', primes)
print('Не простые числа', not_primes)