dp = set()

for x in range(2, 101):
    for y in range(2, 101):
        a = x ** y
        dp.add(a)

print(len(dp))