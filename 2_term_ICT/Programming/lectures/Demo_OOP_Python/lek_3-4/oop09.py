class Super:
    def method(self):
        print('in Super.method')      #	Стандартное поведение
    def delegate(self):
        self.action()                 #	Ожидается определение метода

class Inheritor(Super):
    pass                              #	Буквальное наследование метода

class Replacer(Super):
    def method(self):
        print('in Replacer.method')   #	Полное замещение метода

class Extender(Super):
    def method(self):                 #	Расширение поведения метода
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super):                #	Заполнение обязательного метода
    def action(self):
        print('in Provider.action1')

if  __name__ == '__main__' :
    for klass in (Inheritor, Replacer, Extender):
        print ('\n' + klass.__name__	 + '...')
        klass().method()
        print('\nProvider' )
    x = Provider()
    x = Extender()
    x.delegate()

'''
Если ожидаемый метод в подклассе не определен,
тогда после неудавшегося поиска при наследовании
Python генерирует исключение неопределенного имени
'''



