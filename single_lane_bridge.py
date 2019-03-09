import os
import threading
import random
import argparse
from car import Car
from bridges import *


def create_bridge(type):
    """Creates a Bridge object based on the user's choice."""

    if type == 1:
        bridge = Bridge(1, 'Unsafe-Bridge')
    elif type == 2:
        bridge = SafeBridge(2, 'Safe-Bridge')
    elif type == 3:
        bridge = FairBridge(3, 'Fair-Bridge')
    elif type == 4:
        bridge = AdaptedBridge(4, 'Adapted-Bridge')

    return bridge


def create_cars(bridge, car_limit):
    """Creates Car-Threads equal to the car limit"""

    cars = []
    random_int = random.randint(0, 1)
    i = 0

    while len(cars) < car_limit:
        # Creates red cars
        if random_int == 0:
            cars.append(Car('RedCar', int(i), 'East', bridge))
            i += 1
        # Creates blue cars
        elif random_int == 1:
            cars.append(Car('BlueCar', int(i), 'West', bridge))
            i += 1

        random_int = random.randint(0, 1)

    for car in cars:
        car.join()


def simulate_bridge(bridge_type, car_limit):
    """Simulates the type of bridge the user chose."""

    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the terminal

    bridge = create_bridge(bridge_type)

    print()
    print(
        f'----------------------- {bridge.type} starts -----------------------\n')
    print('West Side\t\tBridge\t\t\tEast side\n')

    create_cars(bridge, car_limit)


def bridge_choice():
    """Gets the input from the user and returns it"""

    bridge_choice = input(
        'Choose which bridge simulation you want to test: ')

    while bridge_choice not in ['1', '2', '3', '4', 'Q', 'q']:
        print('**Error: Please enter a valid option**')
        bridge_choice = input(
            'Choose which bridge simulation you want to test: ')

    return bridge_choice


def main(car_limit):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('[1] Simulates unsafe bridge')
        print('[2] Simulates safe bridge')
        print('[3] Simulates fair bridge')
        print('[4] Simulates adapted bridge')
        print('Press ( Q ) to quit\n')

        choice = bridge_choice()

        if choice in ['1', '2', '3', '4', ]:
            simulate_bridge(int(choice), car_limit)
        elif choice == 'Q' or choice == 'q':
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        print()
        continue_ = input('Do you want to continue testing ? (Y/N) ')
        while continue_ not in ['y', 'Y', 'n', 'N']:
            print('Please type Y or N!')
            continue_ = input('Do you want to continue testing ? (Y/N) ')

        if continue_ == 'n' or continue_ == 'N':
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A command line program that simulates a single lane bridge.')
    parser.add_argument('-c', '--cars', type=int,
                        help='Number of cars to be created.')
    args = parser.parse_args()

    car_limit = args.cars

    if car_limit == None:
        car_limit = 10

    main(car_limit)

    exit(0)
