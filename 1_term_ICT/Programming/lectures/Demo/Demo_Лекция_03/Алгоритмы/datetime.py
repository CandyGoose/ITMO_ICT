import datetime
first_date = datetime.date(2021, 10, 14)

print(first_date.year) # 2021
print(first_date.day)  # 14
print(first_date.month) # 10
print(type(first_date.year))

current_date = datetime.date.today()
print(current_date)
print(current_date.year, type(current_date.year))

delta = current_date - first_date
print(delta, type(delta))

year = current_date.year

if year % 4 != 0:
    print("Обычный")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Високосный")


if year % 400 == 0:
    print("високосный")
elif year % 100 == 0:
    print("не високосный")
elif year % 4 == 0:
    print("високосный")
else:
    print("не високосный")
    

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')


import calendar
print(calendar.isleap(year))
