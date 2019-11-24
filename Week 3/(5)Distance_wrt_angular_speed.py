#Code by Infiltrat8r

def distance(radius,angular_speed,time):

    linear_speed = radius*angular_speed
    print('The speed of the Car is:',linear_speed,'meters per second.')
    dist = linear_speed*time
    print('The distance covered by the car in',time,'seconds will be:',dist,'meters.')

distance(0.2,12.56,10)