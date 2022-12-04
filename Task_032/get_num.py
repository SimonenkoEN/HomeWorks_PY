def get_num(expression):
    exp = expression[1:-1]
    exp = exp.replace(')',' ')
    exp = exp.replace('(',' ')
    numbers = exp.split(' ')
    numbers[0] = float(numbers[0])
    numbers[2] = float(numbers[2])
    return numbers

def get_rational_num(expression):
    exp = expression[1:-1]
    exp = exp.replace(')',' ')
    exp = exp.replace('(',' ')
    numbers = exp.split(' ')
    numbers[0] = numbers[0].split('/')
    numbers[0] = list(map(lambda x: int(x), numbers[0]))
    numbers[2] = numbers[2].split('/')
    numbers[2] = list(map(lambda x: int(x), numbers[2]))
    return numbers

def get_complex_num(complex_num):
    number = []
    sgn = 1
    if complex_num[0] == '-':        
        complex_num = complex_num[1:]
        sgn = -1
    if '+' in complex_num:
        pos = complex_num.index('+')
    elif '-' in complex_num:
        pos = complex_num.index('-')
    num = float(complex_num[:pos])
    inum = float(complex_num[pos+1:-1])
    sign = complex_num[pos]
    if sign == '-':
        inum *= -1
    number.append(num*sgn)
    number.append(inum)
    return number