import math
arr = []
for x in range(999, 99, -1):
    for y in range(x, 99, -1):
        n = x * y
        if str(n) == ''.join(reversed(str(n))):
            arr.append(n)
print(max(arr))
