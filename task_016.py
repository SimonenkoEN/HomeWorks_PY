# Вычислить число π c заданной точностью d
# Пример: при d = 0.001, π = 3.141. 10^-1 ≤ d ≤10^-10
# π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...

print('Задайте степень необходимой точности n (1,0е-n).')
def get_int():
    try:        
        return int(input('Введите натуральное число: '))
    except ValueError:
        print('Введено неверное значение.', end = ' ')
        return get_int()

n = abs(get_int())
accuracy = 10**(-(n+1))
q = 1
s = 1
res_pi = 0
while True:
    a = 4/q
    res_pi += a*s
    q += 2
    s = -s    
    if a < accuracy:
        break
if n != 0:
    print ('pi = ', round(res_pi, n))
else:
    print ('pi = ', round(res_pi))