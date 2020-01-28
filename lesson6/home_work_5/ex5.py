class Stationery:
    def __init__(self, name):
        self.title = name

    def draw(self):
        print(self.title)
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(self.title)
        print('Запуск отрисовки карандашом')


class Pencil(Stationery):
    def draw(self):
        print(self.title)
        print('Запуск отрисовки ручкой')


class Handle(Stationery):
    def draw(self):
        print(self.title)
        print('Запуск отрисовки маркером')


stat = Stationery('Канцелярия')
pen = Pen('Карандаш')
pencil = Pencil('Ручка')
handle = Handle('Маркер')

stat.draw()
pen.draw()
pencil.draw()
handle.draw()
