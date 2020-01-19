import sys

try:
    work_time = float(sys.argv[1])
    rate_hour = float(sys.argv[2])
    premium = float(sys.argv[3])
    print(f'Your salary: {work_time*rate_hour + premium}')
except ValueError:
    print('Incorrect enter!')
except IndexError:
    print('Missing data.\nEnter: \n1-work time per month \n2-rate per hour \n3-premium')


