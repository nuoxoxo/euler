import time
tic = time.time()

def isPalin(num):
    s = str(num)
    #return s == s[::-1]
    return s == ''.join(reversed(s))

# i = 10 ** 32
# counter = 0
# while i != 10000019:
#     print(i)
#     if isPalin(i) and i % 10000019 == 0:
#         counter += 1
#     i -= 1

#base = 109
#ceil = 100000
## test is valid

base = 10000019
mult = 1
ceil = 10 ** 32
cntr = 0

# while True:
#     numb = mult * base
#     print(numb, mult)
#     if isPalin(numb):
#         print(numb)
#         cntr += 1
#     if numb > ceil:
#         break
#     mult += 1

while ceil > base:
    print(ceil)
    if isPalin(ceil):
        if ceil % base == 0:
            cntr += 1
            print(ceil)
    ceil -= 1

toc = time.time()

print(cntr)
print(toc - tic)



