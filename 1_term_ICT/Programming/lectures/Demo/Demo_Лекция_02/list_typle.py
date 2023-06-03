# Зачем нужны кортежи, если есть списки?

# кортеж защищен от изменений
atuple = (1, 2, 3, 4, 5, 6)
blist = [1, 2, 3, 4, 5, 6]
# atuple[1] = 10 # TypeError: 'tuple' object does not support item assignment
blist[1] = 10
print(blist[1]) # 10

# меньший размер

print(atuple.__sizeof__()) # 36
print(blist.__sizeof__()) # 44

# Возможность использовать кортежи в качестве ключей словаря

d = {atuple : 1}
print(d)    # {(1, 2, 3, 4, 5, 6): 1}

d = {atuple[2] : 1}
print(d)    # {3: 1}

# а если захотелось изменить кортеж?
print(atuple, id(atuple))
list2 = list(atuple)
list2[2] = 33
print(list2, id(list2))
atuple = tuple(list2)
print(atuple, id(atuple))



