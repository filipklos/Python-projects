moc = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
karty = [[], [], [], [], [], [], []]

file = open("2023_7.txt")
for i in file:
    reka = i.split()
    reka[0] = [*reka[0]]
    reka[1] = int(reka[1])
    znaki = set(reka[0])
    tmp = []
    for j in znaki:
        tmp.append(reka[0].count(j))
    tmp = sorted(tmp)
    if tmp == [1, 1, 1, 1, 1]:
        karty[0].append(reka)
    if tmp == [1, 1, 1, 2]:
        karty[1].append(reka)
    if tmp == [1, 2, 2]:
        karty[2].append(reka)
    if tmp == [1, 1, 3]:
        karty[3].append(reka)
    if tmp == [2, 3]:
        karty[4].append(reka)
    if tmp == [1, 4]:
        karty[5].append(reka)
    if tmp == [5]:
        karty[6].append(reka)
file.close()
print(karty[0])
for i in range(0, len(karty)):
    for j in range(0, len(karty[i]) - 1):
        for k in range(j + 1, len(karty[i])):
            l = 0
            while l < 5:
                if moc.index(karty[i][j][0][l]) < moc.index(karty[i][k][0][l]):
                    break
                if moc.index(karty[i][j][0][l]) > moc.index(karty[i][k][0][l]):
                    karty[i][j][0], karty[i][k][0] = karty[i][k][0], karty[i][j][0]
                    break
                l += 1

mnorznik = 1
wynik = 0
for i in range(0, len(karty)):
    for j in range(0, len(karty[i])):
        wynik += karty[i][j][1] * mnorznik
        mnorznik += 1
print(wynik)
# 250353952
# 250120186
# 250665248