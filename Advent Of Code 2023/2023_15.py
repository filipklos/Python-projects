plik = open("2023_15.txt")

kody = ""
for i in plik:
    kody += str(i.strip())
plik.close()
kody = kody.split(',')

wynik = 0
for tekst in kody:
    kod = 0
    for i in tekst:
        kod += ord(i)
        kod *= 17
        kod = kod % 256
    wynik += kod
print(wynik)

#Part 2
pudla = [[] for _ in range(256)]
for tekst in kody:
    if tekst[-1] == "-":
        usun = False
        ob = [tekst[:-1], tekst[-1]]
        kod = 0
        for i in ob[0]:
            kod += ord(i)
            kod *= 17
            kod = kod % 256
        for i in range(0, len(pudla[kod])):
            if pudla[kod][i][0] == ob[0]:
                inde = i
                usun = True
        if usun:
            del pudla[kod][inde]
    else:
        ob = [tekst[:-2], int(tekst[-1])]
        kod = 0
        for i in ob[0]:
            kod += ord(i)
            kod *= 17
            kod = kod % 256
        niema = True
        for i in range(0, len(pudla[kod])):
            if pudla[kod][i][0] == ob[0]:
                pudla[kod][i] = ob
                niema = False
        if niema:
            pudla[kod].append(ob)

wynik = 0
for i in range(0, len(pudla)):
    for j in range(0, len(pudla[i])):
        wynik += pudla[i][j][1] * (j + 1) * (i + 1)

print(wynik)