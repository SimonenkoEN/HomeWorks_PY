def get_sum(num1, num2):
    return str(num1+num2)

def get_rational_sum(num1, num2):
    a1 = num1[0]
    b1 = num1[1]
    a2 = num2[0]
    b2 = num2[1]
    m = max(b1,b2)
    numerals = 1
    numeral = 1
    for i in range(1,m+1):
        numeral = min(b1,b2)*i
        if numeral%m == 0:
            a1 = a1 * int(numeral/b1)
            a2 = a2 * int(numeral/b2)
            break
    numerals = a1+a2
    for i in range(abs(numerals),0,-1):
        if numeral%i == 0 and numerals%i == 0:
            numerals = int(numerals/i)
            numeral = int(numeral/i)
            break
    if numerals != 0:
        res = str(numerals)+'/'+str(numeral)
    else:
        res = '0'
    return res

def get_complex_sum(num1, num2):
    num = num1[0] + num2[0]
    inum = num1[1] + num2[1]
    res = str(num)
    if inum > 0:
        res += '+' + str(inum)
    else:
        res += str(inum)
    res += 'i'
    return res