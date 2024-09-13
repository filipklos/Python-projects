plik = open("2023_9.txt")

historie = []
for i in plik:
    linia = [int(j) for j in i.split()]
    historie.append(linia)
plik.close()

wynik = 0
for i in historie:
    historia = [i]
    while True:
        tmp = []
        for j in range(len(historia[len(historia) - 1]) - 1):
            tmp.append(historia[len(historia) - 1][j + 1] - historia[len(historia) - 1][j])
        historia.append(tmp)
        koniec = True
        for liczba in historia[len(historia) - 1]:
            if liczba != 0:
                koniec = False
        if koniec:
            break
    historia[len(historia) - 1].append(0)
    for j in range(len(historia) - 2, -1, -1):
        historia[j].append(historia[j + 1][len(historia[j + 1]) - 1] + historia[j][len(historia[j]) - 1])
    wynik += historia[0][len(historia[0]) - 1]

print(wynik)

#part 2
plik = open("2023_9.txt")

nowe_historie = []
for i in plik:
    linia = [int(j) for j in i.split()]
    nowe_historie.append(linia)
plik.close()

wynik = 0
for i in nowe_historie:
    historia = [i]
    while True:
        tmp = []
        for j in range(len(historia[len(historia) - 1]) - 1):
            tmp.append(historia[len(historia) - 1][j + 1] - historia[len(historia) - 1][j])
        historia.append(tmp)
        koniec = True
        for liczba in historia[len(historia) - 1]:
            if liczba != 0:
                koniec = False
        if koniec:
            break
    historia[len(historia) - 1].insert(0, 0)
    for j in range(len(historia) - 2, -1, -1):
        historia[j].insert(0, historia[j][0] - historia[j + 1][0])
    wynik += historia[0][0]

print(wynik)