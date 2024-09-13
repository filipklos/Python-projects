import sys
sys.set_int_max_str_digits(0)
def fast_power(a, b):
    result = 1
    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2
    return result

print(len(str(fast_power(535323157, 30333))))