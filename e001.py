sum = 0;
for a in range(1, 1001):
    if a % 3 == 0 or a % 5 == 0:
        sum += a;

print(sum);
