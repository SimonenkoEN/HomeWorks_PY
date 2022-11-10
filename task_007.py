# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

from mydef import gin # получение числа типа int с проверкой
from mydef import fact # вычисление факториала

num = abs(gin())
list = []
for i in range(1, num + 1):
    list.append(fact(i))
print(list)