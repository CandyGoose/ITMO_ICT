# применение циклов для подсчета суммы элементов последовательности
lst = [1, 3, 5, 7, 9]
sum1 = 0
for i in lst:
   sum1 += i

print(sum1)


sum2 = 0
while lst:
    sum2 += lst[0]
    lst = lst[1:]

print(sum2)



