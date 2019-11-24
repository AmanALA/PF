# Code by Infiltrat8r

from math import pi
r = eval(input('Enter radius of cylinder in cm: '))
h = eval(input('Enter height of cylinder in cm: '))

vol = lambda : (pi)*((r)**2)*(h)
area = lambda : 2*pi*r*h + 2*pi*(r**2)

print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(vol(),10))
print("The area of the cylinder is {0:.{1}f}cm\u00b2".format(area(),10))

