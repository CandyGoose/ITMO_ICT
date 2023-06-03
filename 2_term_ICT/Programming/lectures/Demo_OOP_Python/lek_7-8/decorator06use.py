def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print(func.__name__, time.time() - t)
        return res
    return wrapper
 
 
def logging(func):
    """
    Декоратор, логирующий работу кода.
    просто выводит вызовы
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print('log ', func.__name__, args, kwargs)
        return res
    return wrapper
 
 
def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper
 
 
@benchmark
@logging
@counter
def reverse_string(string):
    return string[::-1]
 
print(reverse_string("А роза упала на лапу Азора"))
print(reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!"))
 


