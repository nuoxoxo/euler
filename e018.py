a = []
with open('e18.txt')as f:
    for x in f.readlines():
        a.append(x.rstrip('\n').split(' '))


for i in range(len(a) - 1, 0, -1):

    for j in range(0, len(a[i]) - 1):

        x = int(a[i - 1][j]) + int(a[i][j])
        y = int(a[i - 1][j]) + int(a[i][j + 1])


        if x > y:
            a[i - 1][j] = x
        else:
            a[i - 1][j] = y

print(a[0][0])

#### dynamic prog