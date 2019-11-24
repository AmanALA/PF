#Code by Infiltrat8r

import math

def compute_height(length, angle):

    if angle <= 90.0 :
        height = (length)*(math.sin((((angle)*(math.pi))/180)))
        print('\n\nThe Height reached by the Ladder would be :',height,'units.')
    else :
        print('Enter an angle smaller than 90 degrees.....Do you plan to fall off ?')

compute_height(16,75)
compute_height(20,0)
compute_height(24,45)
compute_height(24,80)
