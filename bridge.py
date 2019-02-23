import threading
import time


class Bridge:

    def __init__(self, id):
        self.id = id
        self.lock = threading.Lock()

    def cross(self, car_id):
        self.lock.acquire()
        print(f'*{car_id}* is crossing the bridge')

        try:
            time.sleep(3)
        except InterruptedError:
            print('Interrupted Error')
            exit()
        except KeyboardInterrupt:
            print('Keyboard Interrupt')
            exit()

        print(f'*{car_id}* has crossed the bridge')
        self.lock.release()
