n = 5
k = True
i = 1
while i < n and k:    
    print("Тело цикла")
    k = False
    if (k!=True):
        break
        continue
    i = i + 1   # Увеличение значения переменной-счетчика
    k = True

print("Количество ", i)

