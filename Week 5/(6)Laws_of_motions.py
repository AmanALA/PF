def first_law_of_motion():
    initial_velocity = float(input('Enter initial velocity in m/s: '))
    acceleration = float(input('Enter acceleration in m/s^2: '))
    time = float(input('Enter time taken in seconds: '))
    return (initial_velocity) + (acceleration * time)  # Value of Final velocity


def second_law_of_motion():
    initial_velocity = float(input('Enter initial velocity in m/s: '))
    acceleration = float(input('Enter acceleration in m/s^2: '))
    distance = float(input('Enter distance covered in meters: '))
    return (initial_velocity ** 2) + (2 * acceleration * distance)  # Value of (Final Velocity)^2


def third_law_of_motion():
    initial_velocity = float(input('Enter initial velocity in m/s: '))
    time = float(input('Enter time taken in seconds: '))
    acceleration = float(input('Enter acceleration in m/s^2: '))
    return (initial_velocity * time) + (0.5) * (acceleration) * (time ** 2) #  Value of distance

print(first_law_of_motion())
print(second_law_of_motion())
print(third_law_of_motion())
