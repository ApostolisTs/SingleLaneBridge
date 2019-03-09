import threading
import time


class Bridge:
    """Simulates a bridge with unsafe crossing with crushes."""

    def __init__(self, id, type):
        self.id = id
        self.type = type

    def _crossing_time(self):
        try:
            time.sleep(3)
        except InterruptedError:
            print('Interrupted Error')
            exit(1)
        except KeyboardInterrupt:
            print('Keyboard Interrupt')
            exit(1)

    def cross(self, car):
        if car.direction == 'West':
            print(f'\t\t\t{car.type}-{car.id} is crossing')
            self._crossing_time()
            print(f'\t\t\t\t\t\t{car.type}-{car.id} has crossed')
        elif car.direction == 'East':
            print(f'\t\t\t{car.type}-{car.id} is crossing')
            self._crossing_time()
            print(f'{car.type}-{car.id} has crossed')


class SafeBridge(Bridge):
    """Simulates a bridge with safe crossing. The first one crosses!."""

    def __init__(self, id, type):
        super().__init__(id, type)
        self.lock = threading.Lock()

    def cross(self, car):
        with self.lock:
            super().cross(car)


class FairBridge(Bridge):
    """Simulates a fair bridge with safe crossing.The cars are crossing
    in order one from the west side and one from the other side.
    If no cars are waiting from the west side, east side cars are crossing
    freely, and the opposite.
    """

    def __init__(self, id, type):
        super().__init__(id, type)
        self.blue_cond = threading.Condition()  # Condition variable for blue cars
        self.red_cond = threading.Condition()   # Condition variable for red cars
        self.blue_turn = False
        self.red_turn = False
        self.blues_waiting = 0
        self.reds_waiting = 0

    def blue_crossing(self, car):
        self.blues_waiting += 1

        # Locking the critical section using the with statement
        with self.blue_cond:
            while not self.blue_turn:   # While it's not a blue car's turn
                self.blue_cond.wait()   # Wait until notified

            self.blue_turn = False
            self.blues_waiting -= 1

            super().cross(car)

            with self.red_cond:
                # If red cars are waiting notify them
                if self.reds_waiting > 0:
                    self.red_turn = True
                    self.red_cond.notify_all()
                # else blue cars keep crossing
                else:
                    self.blue_turn = True
                    self.blue_cond.notify_all()

    def red_crossing(self, car):
        self.reds_waiting += 1

        # Locking the critical section
        with self.red_cond:
            while not self.red_turn:    # While it's not a red car's turn
                self.red_cond.wait()    # Wait until notified

            self.red_turn = False
            self.reds_waiting -= 1

            super().cross(car)

            with self.blue_cond:
                # If blue cars are waiting notify them
                if self.blues_waiting > 0:
                    self.blue_turn = True
                    self.blue_cond.notify_all()
                # else red cars keep crossing
                else:
                    self.red_turn = True
                    self.red_cond.notify_all()


class AdaptedBridge(Bridge):
    """Simulates a bridge with safe crossing which adapts on the number of
    the cars waiting. If more cars are waiting in the east side, they start
    crossing the bridge until the cars waiting in the west side are more,
    and the opposite.
    """

    def __init__(self, id, type):
        super().__init__(id, type)
        self.blue_cond = threading.Condition()  # Condition variable for blue cars
        self.red_cond = threading.Condition()   # Condition variable for red cars
        self.blue_turn = False
        self.red_turn = False
        self.blues_waiting = 0
        self.reds_waiting = 0

    def blue_crossing(self, car):
        self.blues_waiting += 1

        # Locking the critical section using the with statement
        with self.blue_cond:
            while not self.blue_turn:   # While it's not a blue car's turn
                self.blue_cond.wait()   # Wait until notified

            self.blue_turn = False
            self.blues_waiting -= 1

            super().cross(car)

            with self.red_cond:
                # If the red cars that are waiting are more
                # than the blue cars let red cars cross the bridge
                if self.reds_waiting > self.blues_waiting:
                    self.red_turn = True
                    self.red_cond.notify_all()

                # Else let blue cars cross the bridge
                else:
                    self.blue_turn = True
                    self.blue_cond.notify_all()

    def red_crossing(self, car):
        self.reds_waiting += 1

        # Locking the critical section
        with self.red_cond:
            while not self.red_turn:    # While it's not a red car's turn
                self.red_cond.wait()    # Wait until notified

            self.red_turn = False
            self.reds_waiting -= 1

            super().cross(car)

            with self.blue_cond:
                # If the blue cars that are waiting are more
                # than the red cars let blue cars cross the bridge
                if self.blues_waiting > self.reds_waiting:
                    self.blue_turn = True
                    self.blue_cond.notify_all()

                # Else let red cars cross the bridge
                else:
                    self.red_turn = True
                    self.red_cond.notify_all()
