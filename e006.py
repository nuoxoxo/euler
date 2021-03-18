a = 0
b = 0

for i in range(101):
    a += i ** 2
    b += i

c = b ** 2 - a

print(a, b, c)