plik = open("2023_18.txt")
instrukcje = []
for i in plik:
    linia = i.split()
    instrukcje.append([linia[0], int(linia[1])])
plik.close()

wiel = 1000
mapa = []
for i in range(wiel):
    tmp = []
    for j in range(wiel):
        tmp.append(".")
    mapa.append(tmp)
mapa[int(wiel / 2)][int(wiel / 2)] = "#"
pisak = [int(wiel / 2), int(wiel / 2)]
for i in instrukcje:
    if i[0] == "U":
        for j in range(i[1]):
            mapa[pisak[0] - j - 1][pisak[1]] = "#"
        pisak[0] = pisak[0] - j - 1
    if i[0] == "D":
        for j in range(i[1]):
            mapa[pisak[0] + j + 1][pisak[1]] = "#"
        pisak[0] = pisak[0] + j + 1
    if i[0] == "L":
        for j in range(i[1]):
            mapa[pisak[0]][pisak[1]  - j - 1] = "#"
        pisak[1] = pisak[1] - j - 1
    if i[0] == "R":
        for j in range(i[1]):
            mapa[pisak[0]][pisak[1]  + j + 1] = "#"
        pisak[1] = pisak[1] + j + 1

for i in range(1, len(mapa) - 1):
    for j in range(1, len(mapa[i]) - 1):
        if mapa[i][j] == ".":
            zu, zd, zl, zr = False, False, False, False
            u = 1
            while i - u >= 0:
                if mapa[i - u][j] == "#":
                    zu = True
                    break
                u += 1
            d = 1
            while i + d < len(mapa):
                if mapa[i + d][j] == "#":
                    zd = True
                    break
                d += 1
            l = 1
            while j - l >= 0:
                if mapa[i][j - l] == "#":
                    zl = True
                    break
                l += 1
            r = 1
            while j + r < len(mapa[i]):
                if mapa[i][j + r] == "#":
                    zr = True
                    break
                r += 1
            if zu and zd and zl and zr:
                mapa[i][j] = "#"

wynik = 0
for i in mapa:
    for j in i:
        if j =="#":
            wynik += 1
print(wynik)