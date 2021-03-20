def sumDiv(n):
    a = []
    i = 1
    while i < n:
        if n % i == 0:
            a.append(i)
        i += 1
    return sum(a)

def isAmica(n):
    a = sumDiv(n)
    b = sumDiv(a)
    if b == n and a != b:
        return 1
    else:
        return 0



arr = set()
w = 10000
for x in range(1, w + 1):
    if isAmica(x) == 1:
        arr.add(x)

print(sum(arr))
