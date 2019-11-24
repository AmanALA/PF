# Code by Infiltrat8r

from math import sin,cos,tan

cos_table = lambda a,b : exec("for i in range(a,b+1): print('The cos of {} is: {}'.format(i,cos(i)))")
sin_table = lambda a,b : exec("for i in range(a,b+1): print('The sin of {} is: {}'.format(i,sin(i)))")
tan_table = lambda a,b : exec("for i in range(a,b+1): print('The tan of {} is: {}'.format(i,tan(i)))")

a= eval(input('Enter first number of range: '))
b = eval(input('Enter second number of range: '))
print(cos_table(a,b),sin_table(a,b),tan_table(a,b),sep='')

