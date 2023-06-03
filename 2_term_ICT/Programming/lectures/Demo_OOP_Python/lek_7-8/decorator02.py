def bread(func):
    def wrapper():
        print("</------\>")
        func()
        print("<\______/>")
    return wrapper
 
def ingredients(func):
    def wrapper():
        print("~помидоры~")
        func()
        print("~салат~")
    return wrapper
 
def sandwich(food="--ветчина--"):
    print(food)
 
sandwich() # выведет: --ветчина--

sandwich = bread(ingredients(sandwich))
sandwich()

# используя синтаксис декораторов:
@bread
@ingredients
def sandwich(food="--ветчина--"):
    print( food)

sandwich()


# порядок декорирования важен:

@ingredients
@bread
def sandwich(food="--ветчина--"):
    print(food)

sandwich()
