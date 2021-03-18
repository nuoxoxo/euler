a = []
with open('e11.txt', 'r') as f:
    for x in f.readlines():
        a.append(x.rstrip('\n').split(' '))
# for x in a:
#     print(x)
###### -->> produce a list of strings

## greatestproduct -->>
gp = 0
for x in range(0, len(a[0]) - 3):
    for y in range(0, len(a[0]) - 3):
        
        n = int(a[x][y]) * int(a[x][y + 1]) * int(a[x][y + 2]) * int(a[x][y + 3])
        if n > gp:
            gp = n
        
        n = int(a[x][y]) * int(a[x + 1][y + 1]) * int(a[x + 2][y + 2]) * int(a[x + 3][y + 3])
        if n > gp:
            gp = n
        
        n = int(a[x][y]) * int(a[x + 1][y]) * int(a[x + 2][y]) * int(a[x + 3][y])
        if n > gp:
            gp = n
        
        if x > 3 :
            n = int(a[x - 1][y + 1]) * int(a[x - 2][y + 2]) * int(a[x - 3][y + 3]) * int(a[x][y])
            if n > gp:
                gp = n
        
print(gp)