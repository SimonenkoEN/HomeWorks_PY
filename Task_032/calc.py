from get_num import *
from get_sum import *
from get_ded import *
from get_mult import *
from get_dev import *

def calc(expression):
    exp = expression.replace(' ','')
    nums = get_num(exp)
    match nums[1]:
        case '+':
            return get_sum(nums[0],nums[2])
        case '-':
            return get_ded(nums[0],nums[2])
        case '*':
            return get_mult(nums[0],nums[2])
        case '/':
            return get_dev(nums[0],nums[2])

def calc_rational(expression):
    exp = expression.replace(' ','')
    nums = get_rational_num(exp)
    match nums[1]:
        case '+':
            return get_rational_sum(nums[0],nums[2])
        case '-':
            return get_rational_ded(nums[0],nums[2])
        case '*':
            return get_rational_mult(nums[0],nums[2])
        case '/':
            return get_rational_dev(nums[0],nums[2])

def calc_complex(expression):
    exp = expression.replace(' ','')
    exp = exp[1:-1]
    exp = exp.replace('(',' ')
    exp = exp.replace(')',' ')
    lst = exp.split(' ')
    num1 = get_complex_num(lst[0])
    num2 = get_complex_num(lst[2])
    match lst[1]:
        case '+':
            return get_complex_sum(num1,num2)
        case '-':
            return get_complex_ded(num1,num2)
        case '*':
            return get_complex_mult(num1,num2)
        case '/':
            return get_complex_dev(num1,num2)

# print(calc_complex('(1+3i)/(5+7i)'))
# print(calc('(0.5)+(0.5)'))
# print(calc_rational('(-3/6)/(2/8)'))