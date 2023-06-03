# Шаблонный метод (Template Method)
# Поведенческий паттерн проектирования, который позволяет подклассам расширять шаги алгоритма, 
# не меняя при этом структуру, объявленную в базовом классе

class ExampleBase():
    def template_method(self):
        self.step_start()
        self.step_one()
        self.step_two()
        self.step_three()
        self.step_end()
 
    def step_one(self):
        raise NotImplementedError()
 
    def step_two(self):
        raise NotImplementedError()
 
    def step_three(self):
        raise NotImplementedError()

    def step_start(self):
        print('start')

    def step_end(self):
        print('end')
 
 
class Example(ExampleBase):
    def step_one(self):
        print('Первый шаг алгоритма')
 
    def step_two(self):
        print('Второй шаг алгоритма')
 
    def step_three(self):
        print('Третий шаг алгоритма')
 
 
example = Example()
example.template_method()
