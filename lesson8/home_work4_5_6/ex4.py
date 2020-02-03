class Storehouse:
    def __init__(self):
        self.obj_in_storehouse = []
        self.obj_in_otd = []

    def coming(self):
        print('Наименование товара: 1 - Принтер, 2 - Ксерокс, 3 - Сканер')
        num = enter_user('Введите номер: ', 1, 3)
        if num == 1:
            model = input('Введите модель принтера: ')
            mark = input('Введите марку принтера: ')
            price = enter_user('Введите стоимость за ед в руб: ', 1, 100000)
            quantity = enter_user('Введите количество: ', 1, 1000)
            format_paper = input('Введите формат бумаги(А3, А4): ')
            type_pr = input('Введите тип принтера(струйныйб лазерный): ')
            type_color = input('Введите формат печати(цв, чб): ')
            self.obj_in_storehouse.append(Printer(model, mark, price, quantity, format_paper, type_pr, type_color))
        elif num == 2:
            model = input('Введите модель ксерокса: ')
            mark = input('Введите марку ксерокса: ')
            price = enter_user('Введите стоимость за ед в руб: ', 1, 100000)
            quantity = enter_user('Введите количество: ', 1, 1000)
            format_paper = input('Введите формат бумаги(А3, А4): ')
            type_color = input('Введите формат печати(цв, чб): ')
            self.obj_in_storehouse.append(Xerox(model, mark, price, quantity, format_paper, type_color))
        elif num == 3:
            model = input('Введите модель сканера: ')
            mark = input('Введите марку сканера: ')
            price = enter_user('Введите стоимость за ед в руб: ', 1, 100000)
            quantity = enter_user('Введите количество: ', 1, 1000)
            format_paper = input('Введите формат бумаги(А3, А4): ')
            self.obj_in_storehouse.append(Scanner(model, mark, price, quantity, format_paper))

    def departure(self):
        print('Товары находятся на складе:')
        for num, el in enumerate(self.obj_in_storehouse, 1):
            print(num, ': ', el)
        num = enter_user('Введите номер товара для отправки в отдел: ', 1, len(self.obj_in_storehouse))
        otd = input('Введите наименование отдела: ')
        my_list = [otd, self.obj_in_storehouse[num-1]]
        self.obj_in_otd.append(my_list)
        del self.obj_in_storehouse[num - 1]
        print('Отправлено')

    def __str__(self):
        print('*'*25 + '\nТовары находятся на складе:')
        for num, el in enumerate(self.obj_in_storehouse, 1):
            print('-'*5 + '\n', num, ': ', el)
        print('*'*25 + '\nТовары находится в отделах: ')
        for num, el in enumerate(self.obj_in_otd, 1):
            print('-'*5 + '\n',num, ': ', el[0], '\n', el[1])
        return ''


class Equipment:
    def __init__(self, model, mark, price, quantity, format_paper):
        self.model = model
        self.mark = mark
        self.price = price
        self.quantity = quantity
        self.format_paper = format_paper


class Printer(Equipment):
    def __init__(self, model, mark, price, quantity, format_paper, type_pr, type_color):
        super().__init__(model, mark, price, quantity, format_paper)
        self.type_pr = type_pr
        self.type_color = type_color

    def __str__(self):
        return f'Принтер {self.model} {self.mark}, в количестве {self.quantity} шт.\n' \
               + f'Тип принтера: {self.type_pr}, {self.format_paper}, {self.type_color};\n' \
                 f'Стоимсость за ед: {self.price}'


class Xerox(Equipment):
    def __init__(self, model, mark, price, quantity, format_paper, type_color):
        super().__init__(model, mark, price, quantity, format_paper)
        self.type_color = type_color

    def __str__(self):
        return f'Ксерокс {self.model} {self.mark}, в количестве {self.quantity} шт.\n' \
               + f'Тип Ксерокса:{self.format_paper}, {self.type_color};\n' \
                 f'Стоимсость за ед: {self.price}'


class Scanner(Equipment):
    def __str__(self):
        return f'Ксерокс {self.model} {self.mark}, в количестве {self.quantity} шт.\n' \
               + f'Тип Ксерокса:{self.format_paper};\n' \
                 f'Стоимсость за ед: {self.price}'


def enter_user(str_in, min_digit, max_digit):
    while True:
        my_str = input(str_in)
        if my_str.isdigit():
            num = int(my_str)
            if min_digit <= num <= max_digit:
                return int(my_str)
            else:
                print('Некорректный ввод')
        else:
            print('Некорректный ввод')


# printer1 = Printer('HP', 'MP112', 12000, 3, 'A3', 'струйный', 'цв')
printer1 = Printer('HP', 'MP112', 12000, 3, 'A3', 'струйный', 'цв')
xerox1 = Xerox('Samsung', 'NP3', 10000, 5, 'A3', 'чб')
storehouse = Storehouse()
storehouse.obj_in_storehouse.append(printer1)
storehouse.obj_in_storehouse.append(xerox1)

while True:
    print('1 - информация о товарах')
    print('2 - приход товара')
    print('3 - уход товара')
    print('0 - выход')
    str_in = enter_user('Введите номер: ', 0, 3)
    if str_in == 0:
        break
    elif str_in == 1:
        print(storehouse)
    elif str_in == 2:
        storehouse.coming()
    elif str_in == 3:
        storehouse.departure()
