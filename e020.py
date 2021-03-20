import math

def fact(n):
    if n > 1:
        return n * fact(n - 1)
    elif n == 1:
        return 1

# base = 10
# fact = fact(base)

# print(fact)

# summ = 0
# while fact != 0:
#     d = fact % 10
#     summ += d
#     print(d, summ)
#     fact = math.floor(fact/10)
    
# print(summ)

### but it's not correct
### why modulo not working here


fact2 = fact(100)
x = list(str(fact2))
# x = (int(i) for i in x)
x = [ int(i) for i in x ]
summ = sum(x)
print(summ)
