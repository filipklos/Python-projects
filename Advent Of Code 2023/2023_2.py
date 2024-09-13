file = open("2023_2.txt")
lista = []
game = []
for i in file:
    tmp = [0, 0, 0]
    j = 5
    while j < len(i):
        if i[j].isdigit():
            if i[j + 1].isdigit():
                if i[j + 3] == "r":
                    tmp[0] += int(i[j] + i[j + 1])
                if i[j + 3] == "g":
                    tmp[1] += int(i[j] + i[j + 1])
                if i[j + 3] == "b":
                    tmp[2] += int(i[j] + i[j + 1])
                j += 2
            else:
                if i[j + 2] == "r":
                    tmp[0] += int(i[j])
                if i[j + 2] == "g":
                    tmp[1] += int(i[j])
                if i[j + 2] == "b":
                    tmp[2] += int(i[j])
                j += 1
        else:
            if i[j] == ";" or i[j] == "\n" or i[j] == ":":
                game.append(tmp[::])
                tmp = [0, 0, 0]
            j += 1
    lista.append(game[1::])
    game.clear()
file.close()

suma = 0
for i in range(0, len(lista)):
    mozliwe = True
    for j in lista[i]:
        if j[0] > 12:
            mozliwe = False
        if j[1] > 13:
            mozliwe = False
        if j[2] > 14:
            mozliwe = False
    if mozliwe:
        suma += i + 1
print(suma)

#part 2
suma = 0
for i in range(0, len(lista)):
    r = 0
    g = 0
    b = 0
    for j in lista[i]:
        if j[0] > r:
            r = j[0]
        if j[1] > g:
            g = j[1]
        if j[2] > b:
            b = j[2]
    suma += r * g * b
print(suma)