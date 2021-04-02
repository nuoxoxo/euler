from datetime import datetime

sun = 0

for y in range(1901, 2001):
    for m in range(1, 13):
        if datetime(y, m, 1).weekday() == 6:
            sun += 1

print(sun)
