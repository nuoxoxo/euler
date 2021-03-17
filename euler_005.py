a = 2520
for x in range(10, 20):
    if a % (x + 1) != 0:
        i = 0
        for y in (2, x + 1):
            if (x + 1) % y == 0 and i < 1:
                a *= y
                i += 1
                
                
print(a)
### produce wrong answer if problem is 1-30 