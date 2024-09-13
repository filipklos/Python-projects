from random import randint
from time import time
start = time()

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        p = lista.pop()
        mniejsze = []
        wieksze = []

        for i in lista:
            if i <= p:
                mniejsze.append(i)
            else:
                wieksze.append(i)
    return quick_sort(mniejsze) + [p] + quick_sort(wieksze)

lista = []
for i in range(0, 100_000):
    lista.append(randint(1, 100_000))
print(lista)
print(quick_sort(lista))
end = time()
print(end - start)
