base = 2
powr = 1000
base = base ** powr

strr = str(base)
summ = 0

for i in range(0, len(strr)):
    summ += int(strr[i])
    
print(summ)