import math

x = 1
c = 0
while True:
    c += 1
    i = 2
    #print(x)

    #for y in range(1, 30):
    for y in range(2, x / 2 + 1):
        if x % y == 0:
            i += 1
    if i > 99:
        print(x, i)
    if i == 500:
        print(x)
        break
    x += c + 1

###print(x) ### Test if it really Breaks :)
### yeah it breaks
### it won't do (x += c + 1)
