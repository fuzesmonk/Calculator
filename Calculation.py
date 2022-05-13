import math
from functions import *

num1 = float(input('Enter First Number: '))
num2 = float(input('Enter Second Number: '))
operation = input('''Choose Operand: 
+ for addition
- for subtraction
/ for division
* for multiplication
''')

if operation == ('+'):
    add(num1, num2)

elif operation == ('-'):
    subtract(num1, num2)

elif operation == ('/'):
    divide(num1, num2)
    
elif operation == ('*'):
    multiply(num1, num2)
else :
    print('Not a valid operand')




