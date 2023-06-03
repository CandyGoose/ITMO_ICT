# Удаление повторов с сохранением порядка
a = [1, 5, 2, 1, 9, 1, 5, 10]
a2 = [1, 5, 2, 1, 9, 1, 5, 10]
a3 = [1, 5, 2, 1, 9, 1, 5, 10]

# Хешируемые типы
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


print(list(dedupe(a)))  # [1, 5, 2, 9, 10]

# Нехешируемые типы
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


print(list(dedupe(a2)))  # [1, 5, 2, 9, 10]

print(list(set(a3))) # [1, 2, 5, 9, 10] - исходный порядок не сохранен
