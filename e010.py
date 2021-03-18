## 2 million 
## 2000000

from math import sqrt

arr = [2, 3]

for x in range(5, 2000000, 2):
    
    counter = 0
    
    ##for y in range(2, x, 1):
    for y in range(2, int(sqrt(x)) + 1):
        if x % y == 0:
            counter += 1
            break
    
    if counter == 0:
        arr.append(x)

print(sum(arr))

## x 142913828925
## 142913828922
