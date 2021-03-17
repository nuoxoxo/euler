def count_bits(n):
    str = bin(n)[2:]
    counter = 0
    for i in str:
        if i == '1':
            counter += 1
    return counter

# if __name__ == '__main__':
#     print(count_bits(1234))