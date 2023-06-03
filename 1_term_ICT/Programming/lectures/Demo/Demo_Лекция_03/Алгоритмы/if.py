# число 1 является логической истиной
if 1:
   print("hello 1")
#elif 2:
#    print("hello 2")

lst = [1, 2, 3]
if lst :
   print("hello 4")

# тернарное выражение
a = 20
b = "Весна" if a > 10 else "Осень"
print(b)

# область допустимых имён
trustName=['Иван', 'Степан', 'Николай']
if 'Степан' in trustName:
   print('Допущен')
else:
   print('Не допущен')

# замена switch с помощью словаря
dp = {"min": -50, "dop": 20, "rab": 30, "max": 55}
choice = "dop"
res = dp[choice]
#res = dp.get(choice, "0") # использование метода get для получения значения по умолчанию
print(res)
