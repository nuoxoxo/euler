def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    x = 0
    y = 0    
    
    for i in walk:
        if i == 'w':
            x -= 1
        elif i == 'e':
            x += 1
        elif i == 'n':
            y -= 1
        elif i == 's':
            y += 1
    if x == 0 and y == 0:
        return True
    return False
#     pass