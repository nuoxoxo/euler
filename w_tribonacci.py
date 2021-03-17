def tribonacci(signature, n):
    a = []
    if n <= 0:
        return [];

    if 1 <= n <= 3:
        for i in range(n):
            a.append(signature[i])
        return a
    if n > 3:
        for i in range(3, n):
                x = signature[i-1]+signature[i-2]+signature[i-3]
                signature.append(x)

    return signature;


# if __name__ == "__main__":
#     a = tribonacci([132, 61, 174], 2)
#     print(a)