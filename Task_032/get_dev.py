def get_dev(num1, num2):
    res = round(num1/num2,3)
    return str(res)

def get_rational_dev(num1, num2):
    a1 = num1[0]
    b1 = num1[1]
    a2 = num2[0]
    b2 = num2[1]
    numerals = a1*b2
    numeral = b1*a2
    for i in range(abs(numerals),0,-1):
        if numeral%i == 0 and numerals%i == 0:
            numerals = int(numerals/i)
            numeral = int(numeral/i)
            break
    res = str(numerals)+'/'+str(numeral)
    return res

def get_complex_dev(num1, num2):
    num = round((num1[0]*num2[0]+num1[1]*num2[1])/(num2[0]**2+num2[1]**2), 2)
    inum = round((num1[1]*num2[0]-num1[0]*num2[1])/(num2[0]**2+num2[1]**2), 2)
    res = str(num)
    if inum > 0:
        res += '+' + str(inum)
    elif inum < 0:
        res += str(inum)
    else:
        return res    
    res += 'i'
    return res