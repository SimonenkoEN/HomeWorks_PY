# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import math
from random import randint

def MultiPairs(l):
    m = []
    for i in range(0, math.ceil(len(l)/2)):
        m.append(l[i] * l[-i - 1])
    print(m)

l1 = [randint(0, 9) for i in range(0, 5)]
print(l1)
MultiPairs(l1)

l2 = [randint(0, 9) for i in range(0, 6)]
print(l2)
MultiPairs(l2)