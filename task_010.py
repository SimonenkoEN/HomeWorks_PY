# Реализуйте алгоритм перемешивания списка.

from random import randint

list = ['a', 'b', 'c', 'd', 'e', 'f']

for i in range(len(list)):
    rnd_i = randint(0, len(list) - 1)
    list[i], list[rnd_i] = list[rnd_i], list[i]
print(list)
