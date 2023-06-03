''' Алгоритм расчета квадратного корня'''
target = 2021
x = 1
oldx = 0
while (oldx != x):
    oldx = x
    x = (x + target / x) / 2

print("x = ", x)
print("x^2 = ", x*x)

def my_sqrt(trg):
    x = 1
    oldx = 0
    while (oldx != x):
        oldx = x
        x = (x + target / x) / 2
    return x

result = my_sqrt(target)
print(result)

def my_out(x, y):
    #s = f'{Результат вычисления корня из {x} равен {y}}'
    s = "Результат вычисления корня из {0} равен {1:.2f}".format(x,y)
    print(s)

my_out(target, result)

''' Проверка элементов списка на четность '''
def if_even(nums):
    '''с флагом проверки'''
    res = True
    for x in nums:
        if x % 2 != 0:
            res = False
            break
    return res

result = if_even([1,4,3,2])
print(result)

def if_even(nums):
    '''без флага проверки'''
    for x in nums:
        if x % 2 != 0:
            return False
    return True

result = if_even([1,4,3,2])
print(result)

def if_even(*nums):
    '''принимает несколько элементов и распаковывает'''
    for x in nums:
        if x % 2 != 0:
            return False
    return True

result = if_even(1,4,3,2)
print(result)

def if_even(nums):
    '''Возврат нескольких значений'''
    for i, x in enumerate(nums):
        if x % 2 != 0:
            return False, i # tuple
    return True

result = if_even([2,4,3,2])
print(result)


print(if_even.__doc__)
