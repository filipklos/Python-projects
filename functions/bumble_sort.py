from random import randint
from time import time
start = time()

def list_sort(numbers):
    for i in range(0, len(numbers) - 2):
        for j in range(i + 1, len(numbers) - 1):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


lista = []
for i in range(0, 10_000):
    lista.append(randint(1, 100_000))
print(lista)
print(list_sort(lista))
end = time()
print(end - start)