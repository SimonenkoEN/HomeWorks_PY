def get_mult(num1, num2):
    return str(num1*num2)

def get_rational_mult(num1, num2):
    a1 = num1[0]
    b1 = num1[1]
    a2 = num2[0]
    b2 = num2[1]
    numerals = a1*a2
    numeral = b1*b2
    for i in range(abs(numerals),0,-1):
        if numeral%i == 0 and numerals%i == 0:
            numerals = int(numerals/i)
            numeral = int(numeral/i)
            break
    res = str(numerals)+'/'+str(numeral)
    return res

def get_complex_mult(num1, num2):
    num = num1[0] * num2[0]
    cnum1 = num1[0] * num2[1]
    cnum2 = num1[1] * num2[0]
    c2num = (num1[1] * num2[1]) * -1
    res = str(num + c2num)
    inum = cnum1 + cnum2
    if inum > 0:
        res += '+' + str(inum)
    else:
        res += str(inum)
    res += 'i'
    return res