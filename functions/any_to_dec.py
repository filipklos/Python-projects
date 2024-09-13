def dec_to_any(num, base):
    number = ""
    while num > 0:
        r = num % base
        num //= base
        number += str(r)
    return number[::-1]

def rec_dec_to_any(num, base):
    if num == 0:
        return ""
    else:
        r = num % base
        return dec_to_any(num // base, base) + str(r)
#1010110
print(dec_to_any(13, 2))
print(rec_dec_to_any(101101, 2))
print(rec_dec_to_any(45, 2))
print(int("1111011", 2))
print(int("2D", 16))