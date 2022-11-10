# Задайте число. Составьте список чисел Фибоначчи, в том числе 
# для отрицательных индексов.

def GetNumber():
    try:
        user_input = int(input('Введите целое число '))
        return user_input
    except ValueError as v:
        print(v)
        return GetNumber()

num = abs(GetNumber())
list = [0 for i in range(0, num*2+1)]
list[num - 1] = list[num + 1] = 1
for i in range(num+2, num*2+1):
    list[i] = list[i-1] + list[i-2]
for i in range(num-2, -1, -1):
    list[i] = list[i+2] - list[i+1]
print(list)
