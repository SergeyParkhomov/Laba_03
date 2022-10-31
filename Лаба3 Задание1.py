from random import randint
import time
n = int(input("Введите количество элементов списка:\n"))
list_a = []
for i in range(n):
    list_a.append(randint(-100, 100))
start1 = time.time()
b = list_a
list_a.sort()
print(*list_a)
end1 = time.time()
print(end1 - start1)
start = time.time()
for i in range(len(b) - 1):
    for j in range(len(b) - i - 1):
        if b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]
print(*b)
end = time.time()
print(end - start)
