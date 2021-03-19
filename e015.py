### need a set of lists, in order to throw out duplicated lists.
### lists are made of tuples
### each tuple is a coordinate of current step taken
### the the answer should be the lenth of the Set
# a = set()
# x = 20
# y = 20
########################
############ 1st attempt

# n = an int
# n = 20
# paths = 0
# x = 0
# while x < n:    ### true length : n + 1
#     if x == 0:
#         y = 1
#         while y < n:
#             if y < n - 1:
#                 paths *= 2
#             else:
#                 print(x, y)

#                 paths += 2
#             y += 1
#     if x > 0 and x < n:
#         y = 0
#         while y < n:
#             if y < n - 1 and x < n - 1:
#                 paths *= 2
#             else:
#                 print(x, y)
#                 paths += 2
#             y += 1
#     x += 1
# print(paths)
########################
############ 2nd attempt


### In fact this is called binomial coefficiant
### binomial coefficient K(a+b,a)
### (a + b)!
### --------
###  a! b!

from math import factorial

n = 20
k = factorial(2 * n) / (factorial(n) * factorial(n))
print(int(k))