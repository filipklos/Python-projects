from math import sqrt

zbior = set()
f = open("1000.txt")
for i in f:
    zbior.add(int(i))
f.close()


def sito(a):
    zbior = set()
    temp = [True] * (a + 1)
    pierw = int(sqrt(a))
    for i in range(2, pierw):
        if temp[i]:
            for j in range(i * i, a + 1, i):
                temp[j] = False
    for i in range(2, a + 1):
        if temp[i]:
            zbior.add(i)
    return zbior


zbior2 = sito(100)
lista = []

for i in zbior:
    if i in zbior2:
        lista.append(i)

print(lista)
