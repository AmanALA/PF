# Code by Infiltrat8r


from math import pi

area = lambda radius: (pi * (radius ** 2)) / 2  # A = π r² / 2

perimeter = lambda radius: (pi * radius) + (radius * 2)  # p = π r + 2 r


print('Area of Semi Circle without Semi Circles included: {0:.{1}f}cm\u00b2'.format(area(14),2))

# I could not find anything as area of a perimeter online, so i just printed the perimeter of a semi circle.

print('Perimeter of Semi Circle without Semi Circles included: {0:.{1}f}cm\u00b2'.format(perimeter(14),2))

# Basically lets assume the two semicircles to have a 7 cm radius.
# -14 (diameter of semi circle) because diameter of inner and outer semi circles exist on same line.

print('Perimeter of Semi Circle with Semi Circles included: {0:.{1}f}cm\u00b2'.format(perimeter(14)+(perimeter(7)-14)+(perimeter(7)-14),2))

print('Area of Semi Circle without Semi Circles included: {0:.{1}f}cm\u00b2'.format(area(14),2))

print('Area of Semi Circle with Semi Circles included: {0:.{1}f}cm\u00b2'.format(area(14)-area(7)-area(7),2))