# [czas, prędkość rekordu]
wyscigi = [[46828479, 347152214061471]]
# wyscigi = [[7, 9], [15, 40], [30, 200]]

kombinacje = 1
for i in wyscigi:
    ilosc = 0
    for j in range (i[0]):
        wyn = j * (i[0] - j)
        if wyn > i[1]:
            ilosc += 1
    kombinacje *= ilosc

print(kombinacje)

#part 2