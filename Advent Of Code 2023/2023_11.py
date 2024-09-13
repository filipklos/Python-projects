plik = open("2023_11.txt")
swiat = []
numer = 1
for i in plik:
    linia = list(i.strip())
    for j in range(0, len(linia)):
        if linia[j] == "#":
            linia[j] = numer
            numer += 1
    swiat.append(linia)
plik.close()


#part 2 - współczynnik rozszerzalności
wspolczynnik = 1



nowy_swiat = []
for i in swiat:
    nowy_swiat.append(i[::])
    poziom = True
    for j in i:
        if isinstance(j, int):
            poziom = False
    if poziom:
        for k in range(wspolczynnik):
            nowy_swiat.append(i[::])

i = 0
while i < len(nowy_swiat[0]):
    pion = True
    for j in nowy_swiat:
        if isinstance(j[i], int):
            pion = False
    if pion:
        for j in nowy_swiat:
            for k in range(wspolczynnik):
                j.insert(i, ".")
        i += wspolczynnik
    i += 1

wsp = []
for i in range(0, len(nowy_swiat)):
    for j in range(0, len(nowy_swiat[i])):
        if isinstance(nowy_swiat[i][j], int):
            wsp.append((i, j))

wynik = 0
for i in range(0, len(wsp) - 1):
    for j in range(i + 1, len(wsp)):
        wynik += abs(wsp[i][0] - wsp[j][0]) + abs(wsp[i][1] - wsp[j][1])

print(wsp)
print(wynik)