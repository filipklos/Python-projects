def NWW(a, b):
    i = j = 1
    while a * i != b * j:
        while a * i < b * j:
            i += 1
        while b * j < a * i:
            j += 1
    return a * i
print(NWW(2, 13))