import threading
import time


class Car(threading.Thread):
    """Simulates a car - thread trying to cross a bridge"""

    def __init__(self, type, id, direction, bridge):
        threading.Thread.__init__(self)
        self.type = type
        self.id = id
        self.direction = direction
        self.bridge = bridge

        self.start()    # Starting the car when the object is created

        try:
            time.sleep(1)
        except InterruptedError:
            print('Interrupted Error')
            exit(1)
        except KeyboardInterrupt:
            print('Keyboard Interrupt')
            exit(1)

    def _print_waiting(self):
        """Prints a car is waiting, on the correct side depending on the car."""

        if self.direction == 'West':
            print(f'{self.type}-{self.id} is waiting')
        elif self.direction == 'East':
            print(f'\t\t\t\t\t\t{self.type}-{self.id} is waiting')

    def run(self):
        if self.bridge.id in [1, 2]:

            self._print_waiting()
            self.bridge.cross(self)

        elif self.bridge.id in [3, 4]:
            self._print_waiting()

            if self.type == 'BlueCar':
                if self.id == 0:
                    self.bridge.blue_turn = True

                self.bridge.blue_crossing(self)
            else:
                if self.id == 0:
                    self.bridge.red_turn = True

                self.bridge.red_crossing(self)
