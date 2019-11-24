# Code by Infiltrat8r
from math import sin,cos

initial_velocity = eval(input('Enter intial velocity in m\s: '))
angle = eval(input('Enter angle of throw in degrees: '))

# Formule are from inter book

compute_height = lambda initial_velocity,angle : (initial_velocity**2)*((sin(angle))**2)/2**(9.8)
time = lambda initial_velocity,angle : (2)*(initial_velocity)*(sin(angle))/(9.8)
range = lambda initial_velocity,angle : ((initial_velocity)**2)/(9.8)

print('Maximum Height of projectile is: {0:.{1}f}m'.format(compute_height(initial_velocity,angle),2))
print('Time of Flight is: {0:.{1}f}m'.format(abs(time(initial_velocity,angle)),2))
print('Maximum Range of projectile or distance covered by projectile is: {0:.{1}f}m'.format(range(initial_velocity,angle),2))

