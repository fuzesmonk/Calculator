import math
from functions import *

def calc(num1, num2) :
    operation = input('''Choose Operand: 
    + for addition
    - for subtraction
    / for division
    * for multiplication
    ''')
    if operation == ('+' '-' '/' '*'):

        num1 = float(input('Enter First Number: '))
        num2 = float(input('Enter Second Number: '))

        if operation == ('+'):
            add(num1, num2)

        elif operation == ('-'):
            subtract(num1, num2)

        elif operation == ('/'):
            divide(num1, num2)

        elif operation == ('*'):
            multiply(num1, num2)


calc(5,5)
