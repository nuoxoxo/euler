# import math
# x = 1
# c = 0
# while True:
#     c += 1
#     i = 2
#     #print(x)

#     #for y in range(1, 30):
#     for y in range(2, int(x / 2 + 1)):
#         if x % y == 0:
#             i += 1
#     if x > 20000000:
#         if i == 500:
#             print(x)
#             break
#     x += c + 1

### seems take forever to run

import math
x = 1
c = 0
while True:
    c += 1
    i = 2


    for y in range(2, int(math.ceil(math.sqrt(x)))):
        if x % y == 0:
            i += 2
    print(x, i)
    if i > 500:
        print(x)
        break
    x += c + 1
    
### runtime: 30s
### Question: when doing int(math.ceil(math.sqrt(x))) why
### should also do ( i += 2 )
### 