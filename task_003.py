# Напишите программу, которая принимает на вход координаты точки 
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

point = [0,0]    
print('Введите координаты точки:')
point[0] = int(input())
point[1] = int(input())
if point[0] > 0 and point[1] > 0:
    print('Точка находится в 1 четверти')
elif point[0] < 0 and point[1] > 0:
    print('Точка находится во 2 четверти')
elif point[0] < 0 and point[1] < 0:
    print('Точка находится в 3 четверти')
elif point[0] > 0 and point[1] < 0:
    print('Точка находится в 4 четверти')
elif point[0] != 0 and point[1] == 0:
    print('Точка находится на оси X')
elif point[0] == 0 and point[1] != 0:
    print('Точка находится на оси Y')
else:
    print('Точка находится в начале координат')