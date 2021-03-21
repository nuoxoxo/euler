selfpow = 0
for x in range(1, 1001):
    selfpow += x ** x

s = str(selfpow)
print(s[len(s)-10:len(s)])
