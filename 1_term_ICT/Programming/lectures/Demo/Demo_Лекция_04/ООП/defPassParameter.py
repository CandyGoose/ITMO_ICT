a = 3
x = [ 1, 2 ]

list11 = [10, 11]

def f1(a):
    a = a + 1
    return a

def f2(a):
    a[0] = a[0] + 1
    return a

def f3(lis):
    lis = lis + [8, 9]
    return lis



print (a)		# 3     Передача по значению
print (x[0])		# 1     Передача по ссылке

print(f1(a))		# 4     Передача по значению
print(f2(x))		# [2, 2]    Передача по ссылке


print(a)		# 3 Передача по значению
print (x[0])		# 2 Передача по ссылке

listn1 = f3(list11)

print(list11)           # [10, 11]

listn2 = f2(list11)

print(listn1)           # [10, 11, 8, 9]

print(list11)           # [11, 11]

print(listn2)           # [11, 11]

