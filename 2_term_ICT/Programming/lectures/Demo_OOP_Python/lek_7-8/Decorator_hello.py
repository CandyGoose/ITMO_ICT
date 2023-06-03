"""
Внутри декораторов makebold() и makeitalic() определили другую функцию wrapped()- обёртку,
которая обёртывает функцию-аргумент и изменяет её поведение.
Декоратор возвращает эту обёртку. 
"""



def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
 
def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


 
@makebold
@makeitalic
def hello():
    return "hello"

def hello_world():
    return "hello world"

 
print(hello())                                    #  <b><i>hello</i></b>

# тоже самое декорирование
hello_world = makebold(makeitalic(hello_world))

print(hello_world())                    # <b><i>hello world</i></b> 
