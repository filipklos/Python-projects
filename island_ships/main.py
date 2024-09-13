plik = open("statki.txt")
lista = []
for x in plik:
    tmp = x.split()
    lista.append(tmp)
plik.close()

maxwspolzedne=str()
maxwiel = 0
for i in range(0, len(lista)):
    wielkosc = 0
    for j in range(0, len(lista[i])):
        if lista[i][j] == '1':
            k=1
            while lista[i][j + k] == '1':
                k+=1
            y=1
            while lista[i+y][j] == '1':
                y+=1
            wielkosc = k*y
            wspolzedne=(i+1, j+1)
            if wielkosc>maxwiel:
                 maxwiel=wielkosc
                 maxwspolzedne = wspolzedne
print(maxwiel)
print(maxwspolzedne)