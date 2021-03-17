sum = 0
arr = []
a = 1
b = 1
while b < 4 * pow(10, 6):
    arr.append(a)
    c = a + b
    a = b
    b = c

for i in arr:
    if i % 2 != 0:
        sum += i

print(sum)
