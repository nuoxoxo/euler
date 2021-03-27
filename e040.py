d = ''
i = 0
while len(d) < 10000001:
    s = str(i)
    d += s
    i += 1

val = int(d[1]) * int(d[10]) * int(d[100]) * int(d[1000]) * int(d[10000]) * int(d[100000]) * int(d[1000000])
print(val)
