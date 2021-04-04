def isprime(x):
    if x == 1 or x == 0:
        return 0
    i = 2
    while i < x / 2:
        if x % i == 0:
            return 0
        i += 1
    return 1

### print all prime numbers under 6 million
# for p in range(2, 6000000):
#     if isprime(p) == 1:
#         print(p)


fp = []
for p in range(2, 6000000):
    counter = 0
    if isprime(p) == 1:
        for a in range(1, p):
            for b in range(1, p):
                for c in range(pow(1, 3), p):
                    if (pow(a,3) + pow(b,3)) % p == pow(c,3) % p:
                        counter += 1
        fp.append(counter)
        print(p, counter)
print(sum(fp))
