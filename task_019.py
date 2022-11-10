# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.

from random import randint

def get_int():
    try:        
        return int(input('Введите натуральное число: '))
    except ValueError:
        print('Введено неверное значение.', end = ' ')
        return get_int()

def get_member(n, max_a): # получение элемента многочлена с рандомным кожффициентом
    a = randint(0, max_a)
    if a == 0:
        return ''
    if a == 1:
        if n == 1:
            return 'x'
        else:
            return 'x^' + str(n)
    elif a > 1:
        if n == 1:
            return str(a) + 'x'
        else:
            return str(a) + 'x^' + str(n)

def get_polynomial(): # формирование строки с меоночленом
    print('Максимальное значение степени многочлена.', end=' ')
    k = abs(get_int())
    print('Максимальное значение кэффициентов многочлена.', end=' ')
    max_k = abs(get_int())
    l = []
    for i in range(k, 0, -1):
        c = get_member(i, max_k)
        if c != '':
            l.append(c)
    # print(l)
    k0 = randint(0, max_k)
    if k0 > 0:
        l.append(str(k0))
    s = '+'.join(l) + '=0'
    return s

s1 = get_polynomial()
print(s1)
with open('file1.txt', 'w') as f1:
    f1.write(s1)

s2 = get_polynomial()
print(s2)
with open('file2.txt', 'w') as f2:
    f2.write(s2)