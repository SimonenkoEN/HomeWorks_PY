# Задайте список из N элементов, заполненных числами из промежутка 
# [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
from mydef import gin # получение числа типа int с проверкой

n = abs(gin())
list = []
list = [i for i in range(-n, n+1)]
print(list)

position = {randint(0, n*2) for i in range(randint(2, n*2))}
print(position)

with open('file.txt', 'w') as f:
    for i in position:
        f.write(str(i))
        f.write('\n')

res = 1
with open('file.txt', 'r') as f:
    for j in f:
        res *= list[int(j)]
print(res)