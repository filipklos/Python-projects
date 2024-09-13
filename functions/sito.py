def sito(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        i = 2
        while i * i <= n:
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
            i += 1
        return primes

lista = sito(10)
for i in range(0, len(lista)):
    if lista[i]:
        print(i)