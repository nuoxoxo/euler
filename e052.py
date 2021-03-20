st = 100001 ### start

while True:
    mult2 = str(st * 2)
    mult3 = str(st * 3)
    mult4 = str(st * 4)
    mult5 = str(st * 5)
    mult6 = str(st * 6)
    if sorted(mult2) == sorted(mult3) and sorted(mult3) == sorted(mult4) and sorted(mult4) == sorted(mult5) and sorted(mult5) == sorted(mult6):
        print(st, st*2, st*3, st*3, st*4, st*5, st*6)
        break
    else:
        st += 1
        

        
    