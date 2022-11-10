# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

l = [7, -6.11, 5.2, 4, 3.01, -2.1, 1]
print(l)

min = max = 0
for i in l:
    if type(i) == float:
        if abs(i)%1 < min or min == 0:
            min = abs(i)%1            
        if abs(i)%1 > max:
            max = abs(i)%1
print(f'max = {round(max, 5)}, min = {round(min, 5)}, max-min = {round(max-min, 5)}')