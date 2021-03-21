import string

with open('e22.txt') as file:
    names = file.read().split(',')
names.sort()

### testing
print(names[2000])
print(names[2000][0])
print(names[2000].strip('"'))
### "HUBERT"

print(string.ascii_uppercase.index(names[2000][1]))
### H in this method = 8
### H in fact = 7


## testing II
letterscore = 0
colin = '"COLIN"'
for x in colin.strip('"'):
    letterscore += string.ascii_uppercase.index(x) + 1
    print(letterscore)

### testing III
# print(names[938]) ### "COLLEEN"
# print(names[937]) ### "COLIN"

totalscore = 0
for x in range(0, len(names)):
    letterscore = 0
    namescore = 0
    for y in names[x].strip('"'):
        letterscore += string.ascii_uppercase.index(y) + 1
        # letterscore += string.ascii_uppercase.index(y)
    namescore = (x + 1) * letterscore
    # print(names[x], namescore)
    totalscore += namescore

print(totalscore)