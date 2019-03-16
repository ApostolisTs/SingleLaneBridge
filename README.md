# Single Lane Bridge

Built in Python 3.7.

It's a program simulating a single lane bridge using threads. One car/thread is allowed to cross
the bridge each time.

#### Cases

- Case 1 - Unsafe Bridge:

    Cars/threads cross the bridge even if another car is crossing from the opposite side.

- Case 2 - Safe Bridge:

    Cars/threads cross the bridge one at a time. Once the bridge is free the *"quickest"* car
    crosses.

- Case 3 - Fair Bridge:

    The stream of cars/threads alternates. For each car coming from the east side another one follows
    from the west. If the last cars are all from the same side and no cars from the opposite side
    are waiting, they all cross the bridge.

- Case 4 - Adapted Bridge:

    Cars/threads cross depending on the traffic. If the cars waiting from the east side are more than
    the cars waiting on the west side, east side cars will cross the bridge until the east side cars
    waiting are less than the ones on the west side.

### Running the program

Type on your terminal or command line:

`python single_lane_bridge.py`

If you want to specify the number of cars/threads you want to be created use the argument `-c`
(default value = 10):

`python single_lane_bridge.py -c 15`
