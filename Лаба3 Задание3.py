import math


def F(n):
    return 1


def F_logn(n):
    coun = 0
    for i in range(int(math.log2(n))):
        coun += 1
    return coun


def F_n2(n):
    coun = 0
    for i in range(n):
        for j in range(n):
            coun += 1
    return coun


def F_2n(n):
    coun = 0
    for i in range(2 ** n):
        coun += 1
    return coun


n = int(input('Введите число n: '))
print(F(n))
print(F_logn(n))
print(F_n2(n))
print(F_2n(n))
