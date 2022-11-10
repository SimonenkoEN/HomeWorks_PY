# Задание 2, задача 1: Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.

from functools import reduce

def get_valid_number(): # проверка введенного числа
    try:
        return float(input('Введите вещественное число '))
    except ValueError:
        print('Введено неверное значение.', end=' ')         
        return get_valid_number()

s = str(abs(get_valid_number()))
lst = list(map((lambda x: int(x)), list(filter((lambda e: (e!='.')), s))))
print(reduce((lambda a, b: a+b), lst))