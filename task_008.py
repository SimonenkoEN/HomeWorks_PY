# Задайте список из n чисел последовательности (1+1/n)^n 
# и выведите на экран их сумму

from mydef import gin # получение числа типа int с проверкой

num = abs(gin())
sum = 0
dic = {i : round((1+1/i)**i, 2) for i in range(1, num + 1)}
print(dic)
for i in dic.values():
    sum += i
print(f'Сумма значений: {sum}')