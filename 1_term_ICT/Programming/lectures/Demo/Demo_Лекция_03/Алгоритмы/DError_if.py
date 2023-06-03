# ошибка
x = -8
if x < -1:
	print('В зону III')
if x > 5:
	print('В зону I')
else:
	print('В зону II')


# нет ошибки
if x < -1:
        print('В зону III')
else:    
    if x > 5:
            print('В зону I')
    else:
            print('В зону II')
