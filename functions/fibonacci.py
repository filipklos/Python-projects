def fib(a):
    ciag = [0, 1]
    for i in range(1, a - 1):
        ciag.append(ciag[i - 1] + ciag[i])
    return ciag

def rec_fib(a):
    if a <= 0:
        return []
    elif a == 1:
        return [0]
    elif a == 2:
        return [0, 1]
    else:
        ciag = fib(a - 1)
        ciag.append(ciag[-1] + ciag[-2])
        return ciag

print(fib(10))
print(rec_fib(10))