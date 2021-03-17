import math

num = 600851475143
#num = 13195
mxp = 0

# if do int(num / 2) process will be killed

for i in range(3, int(math.sqrt(num / 2)), 2):
    if num % i == 0:
        mxp = i
        num /= i



print(mxp)
        

