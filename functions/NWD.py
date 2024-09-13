def NWD(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

def rec_NWD(a, b):
    if b == 0:
        return a
    else:
        return rec_NWD(b, a % b)

print(NWD(24, 32))
print(rec_NWD(24, 32))