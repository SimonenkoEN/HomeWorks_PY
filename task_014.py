# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def GetNumber():
    try:
        user_input = int(input('Введите целое число '))
        return user_input
    except ValueError as v:
        print(v)
        return GetNumber()

num = abs(GetNumber())
n, s = num, ''
while n != 0:
    s = str(n % 2) + s
    n = int(n / 2)
if num < 256: # 0 - 255 выводится в 8-разрядном виде
    s = '0' * (8 - len(s)) + s
print(f'Число {num} в двоичном виде: {s}')
