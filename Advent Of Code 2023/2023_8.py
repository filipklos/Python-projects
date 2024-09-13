kroki = [*"LLLRRRLLRLRLLRRRLRLRRLRRLRRRLRRLLLRLRRLLRLRRRLRRRLLLRLLLLRLRRLLLRRRLRRRLRLRRRLLLLRLRLLRRLLRRRLRRLRLRRRLRRRLLLRLRRRLRRRLRRLLRRLRRRLLRLRLRLRLRLRRRLRLRRLRLRLRLRRLRRLRLRLRRLLRRLRRRLRRLRRLRRRLRRLRLLRLRLLRRLRRRLRLRLRRLLRRLRRRLRRLRRRLRLRRRLRRLRLRRLRLRRLLLRRLRRLRRRLRLRRLRRRLRLRLRRLRLLRRRR"]

plik = open("2023_8.txt")

wezly = []
for i in plik:
    linia = i.split()
    wezly.append([linia[0], [linia[2][1:-1], linia[3][:-1]]])

i = 0
wynik = 0
znaki = "AAA"

while znaki != "ZZZ":
    for j in wezly:
        if j[0] == znaki:
            if kroki[i] == "L":
                znaki = j[1][0]
            elif kroki[i] == "R":
                znaki = j[1][1]
            wynik += 1
            break
    i += 1
    if i == len(kroki):
        i = 0

print(wynik)

#Part 2

znaki = [i[0] for i in wezly if i[0][2] == "A"]
i = 0
wynik = 0

while True:
    for l in range(0, len(znaki)):
        for k in wezly:
            if k[0] == znaki[l]:
                if kroki[i] == "L":
                    znaki[l] = k[1][0]
                elif kroki[i] == "R":
                    znaki[l] = k[1][1]
                break
    wynik += 1
    i += 1
    if i == len(kroki):
        i = 0
    koniec = True
    for j in znaki:
        if j[2] != "Z":
            koniec = False
    if koniec:
        break
print(wynik)
