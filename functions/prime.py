def prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def rec_prime(n, i = 2):
    if n < 2:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return rec_prime(n, i + 1)
print(prime(13))
print(rec_prime(4))