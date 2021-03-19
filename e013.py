a = []
with open('13.txt', 'r') as f:
    for x in f.readlines():
        a.append(x.rstrip('\n'))
som = 0
for x in a:
    som += int(x)
s = str(som)
print(s[:10])