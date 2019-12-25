time = int(input('Enter time in seconds: '))

hh = time // 3600
if hh >= 24:
    hh = hh - (hh // 24)*24
mm = (time % 3600) // 60
ss = time % 60

hh_str = str(hh)
ss_str = str(ss)
mm_str = str(mm)
if hh < 10:
    hh_str = '0' + str(hh)
if mm < 10:
    mm_str = '0' + str(mm)
if ss < 10:
    ss_str = '0' + str(ss)

print(f'{hh_str}:{mm_str}:{ss_str}')