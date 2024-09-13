import time
start = time.time()
file = open("2023_4.txt")
lista = []
for i in file:
    zwycieskie = set()
    wylosowane = set()
    czy_zwycieskie = False
    czy_wylosowane = False
    j = 5
    while j < len(i):
        s_j = j
        if i[j] == ":":
            czy_zwycieskie = True
        if i[j] == "|":
            czy_wylosowane = True
            czy_zwycieskie = False
        if czy_zwycieskie:
            if i[j].isdigit():
                if i[j + 1].isdigit():
                    zwycieskie.add(int(i[j] +i[j + 1]))
                    j += 2
                else:
                    zwycieskie.add(int(i[j]))
                    j += 1
            else:
                j += 1
        if czy_wylosowane:
            if i[j].isdigit():
                if i[j + 1].isdigit():
                    wylosowane.add(int(i[j] +i[j + 1]))
                    j += 2
                else:
                    wylosowane.add(int(i[j]))
                    j += 1
            else:
                j += 1
        if s_j == j:
            j += 1
    tmp = [zwycieskie, wylosowane]
    lista.append(tmp)

suma = 0

for i in range(0, len(lista)):
    potega = -1
    for j in lista[i][1]:
        if j in lista[i][0]:
            potega += 1
    if potega > -1:
        suma += pow(2, potega)
print(suma)
#25010

#Part 2
ilosc = [1 for i in range(0, len(lista))]

for i in range(0, len(lista)):
    razy = ilosc[i]
    trafione = 0
    for j in lista[i][1]:
        if j in lista[i][0]:
            trafione += 1
    for j in range(i + 1, i + 1 + trafione):
        ilosc[j] += razy

suma = 0
for i in ilosc:
    suma += i
print(suma)
#9924412

end = time.time()
print(end - start)