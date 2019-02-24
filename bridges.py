import threading
import time


class Bridge:
    def __init__(self, id):
        self.id = id

    def cross(self, car):
        print(f'{car.id} - Direction: {car.direction} is crossing the {self.id}')

        try:
            time.sleep(3)
        except InterruptedError:
            print('Interrupted Error')
            exit()
        except KeyboardInterrupt:
            print('Keyboard Interrupt')
            exit()

        print(f'{car.id} - Direction: {car.direction} has crossed the {self.id}')


class SafeBridge(Bridge):

    def __init__(self, id):
        super().__init__(id)
        self.lock = threading.Lock()

    def cross(self, car):
        self.lock.acquire()
        super().cross(car)
        self.lock.release()
