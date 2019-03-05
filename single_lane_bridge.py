import os
import threading
import random
from car import Car
from bridges import Bridge, SafeBridge, FairBridge

CAR_LIMIT = 10


def create_bridge(type):
    '''Creates a Bridge object based on the user's choice.'''

    if type == 1:
        bridge = Bridge('Unsafe-Bridge')
    elif type == 2:
        bridge = SafeBridge('Safe-Bridge')
    elif type == 3:
        bridge = FairBridge('Fair-Bridge')

    return bridge


def simulate_bridge(bridge_type):
    '''Simulates the type of bridge the user chose.'''

    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the terminal

    bridge = create_bridge(bridge_type)

    print()
    print(
        f'----------------------- {bridge.id} starts -----------------------\n')
    print('West Side\t\tBridge\t\t\tEast side\n')

    cars = []
    random_int = random.randint(0, 1)
    i = 0

    # Runs until the cars-threads created are equal to the car limit
    while len(cars) < CAR_LIMIT:
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


def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('[1] Simulates unsafe bridge')
        print('[2] Simulates safe bridge')
        print('[3] Simulates fair bridge')
        print('Press ( Q ) to quit\n')

        bridge_choice = input(
            'Choose which bridge simulation you want to test: ')

        while bridge_choice not in ['1', '2', '3', 'Q', 'q']:
            print('**Error: Please enter a valid number**')
            bridge_choice = input(
                'Choose which bridge simulation you want to test: ')

        if bridge_choice == '1':
            simulate_bridge(int(bridge_choice))
        elif bridge_choice == '2':
            simulate_bridge(int(bridge_choice))
        elif bridge_choice == '3':
            simulate_bridge(int(bridge_choice))
        elif bridge_choice == 'Q' or bridge_choice == 'q':
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        print()
        choice = input('Do you want to continue testing ? (Y/N) ')
        while choice not in ['y', 'Y', 'n', 'N']:
            print('Please type Y or N!')
            choice = input('Do you want to continue testing ? (Y/N) ')

        if choice == 'n' or choice == 'N':
            break


if __name__ == '__main__':
    main()
