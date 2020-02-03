import datetime


class Data:
    def __init__(self, data):
        self.data_str = data

    @classmethod
    def conversion_data(cls, data_str):
        '''Data -"01-01-2000'''
        if Data.validation_data(data_str):
            day, month, year = map(int, data_str.split('-'))
            print(f'Day - {day}, Month - {month}, Year - {year}')
            return cls(data_str)
        else:
            print('Incorrect data')

    @staticmethod
    def validation_data(data_str):
        day, month, year = map(int, data_str.split('-'))
        return 31 >= day > 0 and 0 < month <= 12 and 1900 < year <= 2020


my_data = str(datetime.datetime.now().strftime("%d-%m-%Y"))
print('Today', my_data)
dt1 = Data.conversion_data(my_data)
if dt1:
    print(dt1.data_str)

dt2 = Data.conversion_data('31-12-2021')
if dt2:
    print(dt2.data_str)
