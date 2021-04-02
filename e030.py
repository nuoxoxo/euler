import math
arr = []
for n in range(1000,1000000):
    s = [int(x) for x in str(n)]
    a = []
    for i in s:
        j = pow(i, 5)
        a.append(j)
    if sum(a) == n:
        arr.append(n)

print(arr)
print(sum(arr))

#[4150, 4151, 54748, 92727, 93084, 194979]
#443839
