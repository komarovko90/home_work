class Car:
    def __init__(self, speed, col, name, is_police=False):
        self.speed = speed
        self.color = col
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        print(f'Car rides, {speed} km/h')
        self.speed = speed

    def stop(self):
        print(f'Car stop')
        self.speed = 0

    def turn(self, direction):
        print(f'{self.name} turned {direction}')

    def show_speed(self):
        print (f'Your speed: {self.speed}')

    def info_car(self):
        print(self.name, self.color)

class TownCar(Car):
    def __init__(self, speed, col, name):
        super().__init__(speed, col, name)

    def show_speed(self):
        if self.speed > 60:
            print(f'Over speed!! {self.speed}')
            print(f'Police rides after {self.name}!')
            self.is_police = True
        else:
            print(f'Your speed: {self.speed}')


class WorkCar(Car):
    def __init__(self, speed, col, name):
        super().__init__(speed, col, name)

    def show_speed(self):
        if self.speed > 40:
            print (f'Over speed!! {self.speed}')
            print(f'Police rides after {self.name}!')
            self.is_police = True
        else:
            print(f'Your speed: {self.speed}')


class SportCar(Car):
    def __init__(self, speed, col, name):
        super().__init__(speed, col, name)


class PoliceCar(Car):
    def __init__(self, speed, col, name):
        super().__init__(speed, col, name)


vesta = TownCar(35, 'red', 'Vesta')
police = PoliceCar(100, 'blue', 'Police')
porsche = SportCar(110, 'black', 'porsche')
reno = WorkCar(40, 'yellow', 'Reno')

vesta.show_speed()
vesta.go(65)
vesta.show_speed()
vesta.stop()
vesta.show_speed()
vesta.turn('left')
print('-'*40)
police.info_car()
police.show_speed()
print('-'*40)
porsche.info_car()
porsche.show_speed()
print('-'*40)
reno.info_car()
reno.show_speed()
reno.go(45)
reno.show_speed()
