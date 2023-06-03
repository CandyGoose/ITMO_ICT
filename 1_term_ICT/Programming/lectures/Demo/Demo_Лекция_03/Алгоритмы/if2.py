def isQrty(x,y):
    if x > 0:
        if y > 0:               # x > 0, y > 0
            return "Первая четверть"
        else:                   # x > 0, y < 0
            return "Четвертая четверть"
    else:
        if y > 0:               # x < 0, y > 0
            return "Вторая четверть"
        else:                   # x < 0, y < 0
            return "Третья четверть"


if __name__ == "__main__":
	x = 2
	y = 4    
	print(isQrty(x,y))
