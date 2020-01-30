class Worker:
    def __init__(self, name, surname, pos, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = pos
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Full name of employee: {self.name} {self.surname}')
        print(f'Position: {self.position}')

    def get_total_income(self):
        print(f'Income {self.surname}: {self._income["wage"] + self._income["bonus"]}')


empl1 = Position('Brad', 'Pitt', 'Aсtor', 50000, 10000)
empl2 = Position('Marat', 'Safin', 'tennis player', 40000, 5000)

empl1.get_full_name()
empl1.get_total_income()
empl2.get_full_name()
empl2.get_total_income()
