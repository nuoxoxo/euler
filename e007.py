n = 10001
parr = [2]  ## arr of prime nums
x = 3
while len(parr) < n:
    for i in parr:
        if x % i == 0:
            x += 2
            break
    else:
        parr.append(x)

print(max(parr))

## took 17 seconds