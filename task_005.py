# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

def SetCoordinatesPoin():
    point = [0, 0]
    print('Введите координаты точки:')
    point[0] = float(input())
    point[1] = float(input())
    return point

point_A = SetCoordinatesPoin()
point_B = SetCoordinatesPoin()
length_AB = ((point_B[0] - point_A[0])**2 + (point_B[1] - point_A[1])**2)**0.5
print('Длина отрезка равна:', round(length_AB, 2))