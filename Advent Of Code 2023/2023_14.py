plik = open("2023_14.txt")
platforma = []
for i in plik:
    linia = list(i.strip())
    platforma.append(linia)
plik.close()


for i in range(1, len(platforma)):
    for j in range(0, len(platforma[i])):
        if platforma[i][j] == 'O':
            ind = i
            while ind > 0:
                if platforma[ind - 1][j] == '.':
                    platforma[ind][j] = '.'
                    platforma[ind - 1][j] = 'O'
                    ind -= 1
                else:
                    break

waga = 0
for i in range(0, len(platforma)):
    for j in platforma[i]:
        if j == 'O':
            waga += len(platforma) - i
print(waga)