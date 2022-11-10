def gin(): # get valid int number
    try:
        return int(input('Введите целое число '))         
    except ValueError:
        print('Введено неверное значение.', end=' ')         
        return gin()

def gfn(): # get valid float number
    try:
        return float(input('Введите вещественное число '))
    except ValueError:
        print('Введено неверное значение.', end=' ')         
        return gfn()

def fact(n): # get factorial
    if n == 0:
        return 1    
    return fact(n-1)*n
