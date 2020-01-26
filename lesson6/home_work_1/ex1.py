import time
import itertools


class TrafficLight:
    __color = ['red', 'yellow', 'green', 'yellow']

    def running(self):
        count = 0
        for el in itertools.cycle(TrafficLight.__color):
            if count > 6:
                break
            if el == 'red':
                time_counter = 7
                print('\033[31mRed light', end='')
                print(f'\033[37m is on now. Wait {time_counter} seconds.')
                TrafficLight.__pause(self, time_counter)
            elif el == 'green':
                time_counter = 5
                print('\033[32mGreen light', end='')
                print(f'\033[37m is on now. GO! {time_counter} seconds left.')
                TrafficLight.__pause(self, time_counter)
            elif el == 'yellow':
                time_counter = 2
                print('\033[33mYellow light', end='')
                print(f'\033[37m is on now. Ready! {time_counter} seconds left.')
                TrafficLight.__pause(self, time_counter)
            count += 1
        print('The traffic light has broken.')

    def __pause(self, sec):
        count_sym = 0
        while sec > 0:
            print(f'{int(sec)}', end=f'{"." * count_sym}')
            count_sym = count_sym + 1 if count_sym <= 2 else 0
            sec -= 0.5
            time.sleep(0.5)
            print('\r', end='')


tr = TrafficLight()
tr.running()
