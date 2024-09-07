def sieve(n):
    primes = []
    for i in range(2, n+1):
        primes.append(i)
    for i in range(2, n+1):
        if i in primes:
            for j in range(i+i, n+1, i):
                if j in primes:
                    primes.remove(j)
    return primes

print(sieve(100))


def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd2(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(10, 20))
print(gcd2(10, 20))