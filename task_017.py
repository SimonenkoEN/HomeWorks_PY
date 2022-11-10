# Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.

def get_int():
    try:        
        return int(input('Введите натуральное число: '))
    except ValueError:
        print('Введено неверное значение.', end = ' ')
        return get_int()

def check_simple(n):
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
    return True

n = abs(get_int())
l = [1]
d = 2
while d <= n:
    if not (n % d) and check_simple(d):
        l.append(d)
    d += 1
print(l)