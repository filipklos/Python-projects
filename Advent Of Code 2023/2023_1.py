file = open('2023_1.txt')
lista = [list(i.strip()) for i in file]
file.close()
zbior = set('0123456789')

suma = 0
for i in lista:
    liczba = ""
    for j in i:
        if j in zbior:
            liczba += j
            break
    for j in i[::-1]:
        if j in zbior:
            liczba += j
            break
    if liczba != "":
        suma += int(liczba)
print(suma)

# Part 2

def zamien_cyfry(slowo):
    nowe_slowo = ""
    slowa = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(0, len(slowo) - 1):
        znaleziono = False
        if slowo[i].isdigit():
            nowe_slowo += slowo[i]
            break
        proba = ""
        for j in range(i, len(slowo)):
            proba += slowo[j]
            if len(proba) > 5:
                break
            if proba in slowa:
                znaleziono = True
                for k in range(1, 10):
                    if slowa[k - 1] == proba:
                        nowe_slowo += str(k)
                        break
                break
        if znaleziono:
            break

    slowo = slowo[::-1]

    for i in range(0, len(slowo) - 1):
        znaleziono = False
        if slowo[i].isdigit():
            nowe_slowo += slowo[i]
            break
        proba = ""
        for j in range(i, len(slowo)):
            proba += slowo[j]
            if len(proba) > 5:
                break
            if proba[::-1] in slowa:
                znaleziono = True
                for k in range(1, 10):
                    if slowa[k - 1] == proba[::-1]:
                        nowe_slowo += str(k)
                        break
                break
        if znaleziono:
            break
    if len(nowe_slowo) == 1:
        nowe_slowo = nowe_slowo + nowe_slowo
    return nowe_slowo

file = open('2023_1.txt')
lista = [i.strip() for i in file]
file.close()

suma = 0
for i in lista:
    liczba = int(zamien_cyfry(i))
    suma += liczba
print(suma)
#54019