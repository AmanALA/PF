# Code by Infiltrat8r

def dist_by_car(vi, accelaration, time):
    initial_velocity = vi / 3600
    a = accelaration / 3600
    t = ((time * 60) * 60)
    s = ((initial_velocity) * (t)) + ((1 / 2) * (a) * (t * t)) # Using newton second equation
    print('Distance is:', s, 'Miles')


# Input is in (miles per hour),(miles per hour) and (hours)
dist_by_car(50, 10, 2)
