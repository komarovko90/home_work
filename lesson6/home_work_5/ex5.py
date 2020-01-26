class Stationery:
    title = ''

    def draw(self):
        print(self.title)
        print('Запуск отрисовки')

    def __init__(self, name):
        self.title = name


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
