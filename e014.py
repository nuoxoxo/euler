import time

m = 1000000
# n = 13
maxstep = 0

def findsteps(n):
    steps = 1
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
            steps += 1
        else:
            n = 3 * n + 1
            steps += 1
    return steps

tic = time.perf_counter()
for n in range(m, 1, -1):
    steps = findsteps(n)
    if maxstep < steps:
        maxstep = steps
        print(n)
    
print(maxstep)
toc = time.perf_counter()
elap = toc - tic
print(elap)
### elap = 48+ s