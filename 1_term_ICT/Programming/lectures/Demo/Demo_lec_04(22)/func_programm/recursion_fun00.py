
def check(n):
    '''функция рекурсивно определяет четное или нечетное число'''
    if n < 2:
        return (n % 2 == 0)
    return check(n - 2)

  
def sum_number(n):
    """
    сумма числовой последовательности
    """
    if n == 1:
        return 1
    else:
        return n + sum_number(n - 1)

def sum_numbers(nlist):
    ''' Что такое сумма чисел?
    Это есть результат сложения первого элемента
    списка с суммой оставшейся части списка, и кроме того,
    если список пуст, то сумма равна нулю
    '''
    if nlist == []:
        return 0
    else:
        return nlist[0] + sum_numbers(nlist[1:]) 

    
def nod(a,b):
    """
    алгоритм евклида
    """
    if b == 0:
        return a
    else:
        return nod(b, a%b)



n = int(input("число?: "))
nlist = list(range(1,n+1))
nlist2 = [1,2,4,5,6,54,32]

print("Для n = {} Sn = {}".format(n, sum_number(n)))
print("Для n = {} Sn = {}".format(len(nlist), sum_numbers(nlist)))
print("Для {} Sn = {}".format(nlist2, sum_numbers(nlist2)))

k1, k2 = 18, 24
print('НОД', nod(k1, k2))
      
