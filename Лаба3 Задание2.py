def F_3n(n):
    a = []
    coun = 0
    for i in range(n):
        a.append(i)
        coun += 1
    for i in range(n):
        a[i] += 12
        coun += 1
    for i in range(n):
        a[i] //= 2
        coun += 1
    return coun


def F_nlogn(n, x):
    left = 0
    right = n
    a = []
    coun = 0
    for i in range(n):
        a.append(i)
        coun += 1
    while left < right - 1:
        middle = (left + right) // 2
        coun += 1
        if x < a[middle]:
            right = middle
            coun += 1
        else:
            left = middle
            coun += 1
    if a[left] == x:
        print("Номер элемента в списке: ", a.index(x) + 1)
    else:
        print("Элемент не найден")
    return coun


def F_nfac(n):
    global counfac
    if n == 0:
        return 1
    counfac += 1
    return F_nfac(n - 1) * n


def F_n3(n):
    coun = 0
    for i in range(n):
        for j in range(n):
            for q in range(n):
                coun += 1
    return coun


counfac = 1
n = int(input("Введите значение n: "))
x = int(input("Введите значение x: "))
print(F_3n(n))
print(F_nlogn(n, x))
print(F_nfac(n))
print(counfac)
print(F_n3(n))

