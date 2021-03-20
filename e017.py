### 1--9
onetonine = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
len1to9 = 0
for x in onetonine:
    len1to9 += len(x)

print(len1to9)

### 10-19
tentonineteen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', ]
len10to19 = 0
for x in tentonineteen:
    len10to19 += len(x)

print(len10to19)

### 20--99
twentyto90 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
### modif : count no hyphens
len20to99 = 0
for x in twentyto90:
    # sum20to99 += len(x) - 1
    len20to99 += len(x)
    for y in onetonine:
        len20to99 += len(x) + len(y)

print(len20to99)

### 100-999

# hundredand = len('hundredand')
### thewordhundred= 7
### thewordand = 3   ### 10
len100to999 = 11    ### one thousand is 11 words

for x in onetonine:
    len100to999 += 7 + len(x)
    for y in twentyto90:
        len100to999 += 10 + len(x) + len(y)
        for z in onetonine:
            len100to999 += len(x) + 10 + len(y) + len(z)
    for y in tentonineteen:
        len100to999 += len(x) + 10 + len(y)
    for y in onetonine:
        len100to999 += len(x) + 10 + len(y)

print(len100to999)

final = len1to9 + len10to19 + len20to99 + len100to999

print(final)
# 36
# 70
# 748
# 20270
# 21124