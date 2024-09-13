file = open("2023_3.txt")
lista = []
zbior = set()
for i in file:
    lista.append(list(i))
    for j in i:
        if not j.isdigit() and j != "." and j != "\n":
            zbior.add(j)
file.close()


suma = 0
for i in range(1, len(lista) - 1):
    j = 1
    while j < len(lista[i]) - 2:
        stare_j = j
        graniczy = False
        if lista[i][j].isdigit() and not lista[i][j + 1].isdigit():
            liczba = int(lista[i][j])
            for k in range(j - 1, j + 2):
                if lista[i - 1][k] in zbior:
                    graniczy = True
            if lista[i][j - 1] in zbior or lista[i][j + 1] in zbior:
                graniczy = True
            for k in range(j - 1, j + 2):
                if lista[i + 1][k] in zbior:
                    graniczy = True
            j += 1
        if lista[i][j].isdigit() and lista[i][j + 1].isdigit() and not lista[i][j + 2].isdigit():
            liczba = int(lista[i][j] + lista[i][j + 1])
            for k in range(j - 1, j + 3):
                if lista[i - 1][k] in zbior:
                    graniczy = True
            if lista[i][j - 1] in zbior or lista[i][j + 2] in zbior:
                graniczy = True
            for k in range(j - 1, j + 3):
                if lista[i + 1][k] in zbior:
                    graniczy = True
            j += 2
        if lista[i][j].isdigit() and lista[i][j + 1].isdigit() and lista[i][j + 2].isdigit():
            liczba = int(lista[i][j] + lista[i][j + 1] + lista[i][j + 2])
            for k in range(j - 1, j + 4):
                if lista[i - 1][k] in zbior:
                    graniczy = True
            if lista[i][j - 1] in zbior or lista[i][j + 3] in zbior:
                graniczy = True
            for k in range(j - 1, j + 4):
                if lista[i + 1][k] in zbior:
                    graniczy = True
            j += 3
        if j == stare_j:
            j += 1
        if graniczy:
            suma += liczba
print(suma)
#527446

#Part 2
suma = 0
for i in range(1, len(lista) - 1):
    for j in range(1, len(lista[i]) - 1):
        if lista[i][j] == "*":
            liczby = []
            #po lewej
            if lista[i][j - 1].isdigit() and not lista[i][j - 2].isdigit():
                liczby.append(int(lista[i][j - 1]))
            if lista[i][j - 1].isdigit() and lista[i][j - 2].isdigit() and not lista[i][j - 3].isdigit():
                liczby.append(int(lista[i][j - 1] + lista[i][j - 2]))
            if lista[i][j - 1].isdigit() and lista[i][j - 2].isdigit() and lista[i][j - 3].isdigit():
                liczby.append(int(lista[i][j - 1] + lista[i][j - 2] + lista[i][j - 3]))
            #po prawej
            if lista[i][j + 1].isdigit() and not lista[i][j + 2].isdigit():
                liczby.append(int(lista[i][j + 1]))
            if lista[i][j + 1].isdigit() and lista[i][j + 2].isdigit() and not lista[i][j + 3].isdigit():
                liczby.append(int(lista[i][j + 1] + lista[i][j + 2]))
            if lista[i][j + 1].isdigit() and lista[i][j + 2].isdigit() and lista[i][j + 3].isdigit():
                liczby.append(int(lista[i][j + 1] + lista[i][j + 2] + lista[i][j + 3]))
            #na górze
                #1 cyfrowe
            if lista[i - 1][j - 1].isdigit() and not lista[i - 1][j - 2].isdigit() and not lista[i - 1][j].isdigit():
                lista.append(int(lista[i - 1][j - 1]))
            if lista[i - 1][j].isdigit() and not lista[i - 1][j - 1].isdigit() and not lista[i - 1][j + 1].isdigit():
                lista.append(int(lista[i - 1][j]))
            if lista[i - 1][j + 1].isdigit() and not lista[i - 1][j].isdigit() and not lista[i - 1][j + 2].isdigit():
                lista.append(int(lista[i - 1][j + 1]))
                #2 cyfrowe
            if lista[i - 1][j - 1].isdigit() and lista[i - 1][j - 2].isdigit() and not lista[i - 1][j - 3].isdigit() and not lista[i - 1][j].isdigit():
                lista.append(int(lista[i - 1][j - 2] + lista[i - 1][j - 1]))
            if lista[i - 1][j - 1].isdigit()and lista[i - 1][j].isdigit() and not lista[i - 1][j - 2].isdigit()  and not lista[i - 1][j + 1].isdigit():
                lista.append(int(lista[i - 1][j - 1] + lista[i - 1][j]))
            if lista[i - 1][j].isdigit()and lista[i - 1][j + 1].isdigit() and not lista[i - 1][j - 1].isdigit()  and not lista[i - 1][j + 2].isdigit():
                lista.append(int(lista[i - 1][j] + lista[i - 1][j + 1]))
            if lista[i - 1][j + 1].isdigit()and lista[i - 1][j + 2].isdigit() and not lista[i - 1][j].isdigit()  and not lista[i - 1][j + 3].isdigit():
                lista.append(int(lista[i - 1][j + 1] + lista[i - 1][j + 2]))
                # 3 cyfrowe
            if lista[i - 1][j - 3].isdigit() and lista[i - 1][j - 2].isdigit() and lista[i - 1][j - 1].isdigit() and not lista[i - 1][j - 4].isdigit() and not lista[i - 1][j].isdigit():
                lista.append(int(lista[i - 1][j - 3] + lista[i - 1][j - 2] + lista[i - 1][j - 1]))
            if lista[i - 1][j - 2].isdigit() and lista[i - 1][j - 1].isdigit() and lista[i - 1][j].isdigit() and not lista[i - 1][j - 3].isdigit() and not lista[i - 1][j + 1].isdigit():
                lista.append(int(lista[i - 1][j - 2] + lista[i - 1][j - 1] + lista[i - 1][j]))
            if lista[i - 1][j - 1].isdigit() and lista[i - 1][j].isdigit() and lista[i - 1][j + 1].isdigit() and not lista[i - 1][j - 2].isdigit() and not lista[i - 1][j + 2].isdigit():
                lista.append(int(lista[i - 1][j - 1] + lista[i - 1][j] + lista[i - 1][j + 1]))
            if lista[i - 1][j].isdigit() and lista[i - 1][j + 1].isdigit() and lista[i - 1][j + 2].isdigit() and not lista[i - 1][j - 1].isdigit() and not lista[i - 1][j + 3].isdigit():
                lista.append(int(lista[i - 1][j] + lista[i - 1][j + 1] + lista[i - 1][j + 2]))
            if lista[i - 1][j + 1].isdigit() and lista[i - 1][j + 2].isdigit() and lista[i - 1][j + 3].isdigit() and not lista[i - 1][j].isdigit() and not lista[i - 1][j + 4].isdigit():
                lista.append(int(lista[i - 1][j + 1] + lista[i - 1][j + 2] + lista[i - 1][j + 3]))
            # na dole
                #1 cyfrowe
            if lista[i + 1][j - 1].isdigit() and not lista[i + 1][j - 2].isdigit() and not lista[i + 1][j].isdigit():
                lista.append(int(lista[i + 1][j - 1]))
            if lista[i + 1][j].isdigit() and not lista[i + 1][j - 1].isdigit() and not lista[i + 1][j + 1].isdigit():
                lista.append(int(lista[i + 1][j]))
            if lista[i + 1][j + 1].isdigit() and not lista[i + 1][j].isdigit() and not lista[i + 1][j + 2].isdigit():
                lista.append(int(lista[i + 1][j + 1]))
                #2 cyfrowe
            if lista[i + 1][j - 1].isdigit() and lista[i + 1][j - 2].isdigit() and not lista[i + 1][j - 3].isdigit() and not lista[i + 1][j].isdigit():
                lista.append(int(lista[i + 1][j - 2] + lista[i + 1][j - 1]))
            if lista[i + 1][j - 1].isdigit()and lista[i + 1][j].isdigit() and not lista[i + 1][j - 2].isdigit()  and not lista[i + 1][j + 1].isdigit():
                lista.append(int(lista[i + 1][j - 1] + lista[i + 1][j]))
            if lista[i + 1][j].isdigit()and lista[i + 1][j + 1].isdigit() and not lista[i + 1][j - 1].isdigit()  and not lista[i + 1][j + 2].isdigit():
                lista.append(int(lista[i + 1][j] + lista[i + 1][j + 1]))
            if lista[i + 1][j + 1].isdigit()and lista[i + 1][j + 2].isdigit() and not lista[i + 1][j].isdigit()  and not lista[i + 1][j + 3].isdigit():
                lista.append(int(lista[i + 1][j + 1] + lista[i + 1][j + 2]))
                # 3 cyfrowe
            if lista[i + 1][j - 3].isdigit() and lista[i + 1][j - 2].isdigit() and lista[i + 1][j - 1].isdigit() and not lista[i + 1][j - 4].isdigit() and not lista[i + 1][j].isdigit():
                lista.append(int(lista[i + 1][j - 3] + lista[i + 1][j - 2] + lista[i + 1][j - 1]))
            if lista[i + 1][j - 2].isdigit() and lista[i + 1][j - 1].isdigit() and lista[i + 1][j].isdigit() and not lista[i + 1][j - 3].isdigit() and not lista[i + 1][j + 1].isdigit():
                lista.append(int(lista[i + 1][j - 2] + lista[i + 1][j - 1] + lista[i + 1][j]))
            if lista[i + 1][j - 1].isdigit() and lista[i + 1][j].isdigit() and lista[i + 1][j + 1].isdigit() and not lista[i + 1][j - 2].isdigit() and not lista[i + 1][j + 2].isdigit():
                lista.append(int(lista[i + 1][j - 1] + lista[i + 1][j] + lista[i + 1][j + 1]))
            if lista[i + 1][j].isdigit() and lista[i + 1][j + 1].isdigit() and lista[i + 1][j + 2].isdigit() and not lista[i + 1][j - 1].isdigit() and not lista[i + 1][j + 3].isdigit():
                lista.append(int(lista[i + 1][j] + lista[i + 1][j + 1] + lista[i + 1][j + 2]))
            if lista[i + 1][j + 1].isdigit() and lista[i + 1][j + 2].isdigit() and lista[i + 1][j + 3].isdigit() and not lista[i + 1][j].isdigit() and not lista[i + 1][j + 4].isdigit():
                lista.append(int(lista[i + 1][j + 1] + lista[i + 1][j + 2] + lista[i + 1][j + 3]))
            if len(liczby) == 2:
                suma += liczby [0] * liczby [1]
print(suma)
#73201705
