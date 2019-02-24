import os
import threading
import random
from car import Car
from bridges import Bridge, SafeBridge

CAR_LIMIT = 10


def implement_bridge(bridge_type):
    os.system('cls' if os.name == 'nt' else 'clear')

    if bridge_type == 1:
        bridge = Bridge('Unsafe-Bridge')
    elif bridge_type == 2:
        bridge = SafeBridge('Safe-Bridge')

    print()
    print(f'---------- {bridge.id} starts ----------\n')

    # This way the cars are crossing the bridge in order! WHY ?
    # red_cars = [Car(f'RedCar{i}', 'South', bridge) for i in range(5)]
    # blue_cars = [Car(f'BlueCar{i}', 'North', bridge) for i in range(5)]

    cars = []
    random_int = random.randint(0, 1)
    i = 0

    # Runs until the cars-threads created are equal to the car limit
    while len(cars) < CAR_LIMIT:
        if random_int == 0:
            # Creates red cars
            cars.append(Car(f'RedCar{i}', 'South', bridge))
            i += 1
        elif random_int == 1:
            # Creates blue cars
            cars.append(Car(f'BlueCar{i}', 'North', bridge))
            i += 1

        random_int = random.randint(0, 1)

    for car in cars:
        car.join()


def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('[1] Implements unsafe bridge')
        print('[2] Implements safe bridge')
        print('Press ( Q ) to quit\n')

        bridge_choice = input(
            'Choose the bridge implementation you want to test: ')

        while bridge_choice not in ['1', '2', 'Q', 'q']:
            print('**Error: Please enter a valid number**')
            bridge_choice = input(
                'Choose the bridge implementation you want to test: ')

        if bridge_choice == '1':
            implement_bridge(int(bridge_choice))
        elif bridge_choice == '2':
            implement_bridge(int(bridge_choice))
        elif bridge_choice == 'Q' or bridge_choice == 'q':
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        print()
        choice = input('Do you want to continue testing ? (Y/N) ')
        if choice == 'n' or choice == 'N':
            break


if __name__ == '__main__':
    main()
