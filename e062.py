arr = []
d = {}
i = 2

while True:
    a = i ** 3
    b = sorted(list(str(a)))
    if b not in arr:
        arr.append(b)
        d[a] = 1
    else:
        for x in d:
            if b == sorted(list(str(x))):
                d[x] += 1
                break
        if d[x] == 5:
            thisIsIt = x
            break
    i += 1

print(thisIsIt)

