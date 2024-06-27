def findGCD(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1
findGCD(6, 4)
findGCD(5, 16)
findGCD(12, 6)