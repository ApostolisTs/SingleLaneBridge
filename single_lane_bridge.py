import threading
from car import Car
from bridge import Bridge
import random

CAR_LIMIT = 5

print('---------- Single Lane Bridge starts ----------\n')
red_car_ctr = 0
blue_car_ctr = 0
random_int = random.randint(0, 1)
bridge = Bridge('Unsafe bridge')

# This way the cars are crossing the bridge in order! WHY ?

# red_cars = [Car(f'RedCar{i}', 'South', bridge) for i in range(5)]
# blue_cars = [Car(f'BlueCar{i}', 'North', bridge) for i in range(5)]

# Checks if the cars have crossed the limit
while red_car_ctr < CAR_LIMIT or blue_car_ctr < CAR_LIMIT:
    # Creates red cars
    if random_int == 0 and red_car_ctr < CAR_LIMIT:
        car = Car(f'RedCar{red_car_ctr}', 'South', bridge)
        red_car_ctr += 1
    # Creates red cars
    elif random_int == 1 and blue_car_ctr < CAR_LIMIT:
        car = Car(f'BlueCar{blue_car_ctr}', 'North', bridge)
        blue_car_ctr += 1

    random_int = random.randint(0, 1)

print('---------- Single Lane Bridge ends ----------\n')
