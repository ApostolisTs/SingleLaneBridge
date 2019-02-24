import threading
import time


class Car(threading.Thread):

    def __init__(self, id, direction, bridge):
        threading.Thread.__init__(self)
        self.id = id
        self.direction = direction
        # if direction == 'South':
        #     self.direction = 0
        # else:
        #     self.direction = 1
        self.bridge = bridge

        try:
            time.sleep(1)
        except InterruptedError:
            print('Interrupted Error')
            exit()

        except KeyboardInterrupt:
            print('Keyboard Interrupt')
            exit()

        self.start()

    def run(self):
        print(
            f'{self.id}-Direction:{self.direction} is waiting to cross the {self.bridge.id}')
        self.bridge.cross(self)
