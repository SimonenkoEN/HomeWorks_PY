# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

from random import randint

l = [randint(0, 9) for i in range(10)]
print(l)
leng = len(l)-1
i = 0
while i < leng:
    j = leng
    while j > i:
        if l[i] == l[j]:
            l.pop(j)
            leng -= 1
        j -= 1
    i += 1
print(l)