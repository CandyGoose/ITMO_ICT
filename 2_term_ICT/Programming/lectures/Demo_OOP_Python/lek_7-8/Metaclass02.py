""" type принимает на вход описание класса и возвращает класс
Синтаксис:
  type(<имя класса>, 
       <кортеж родительских классов>,      # для наследования, может быть пустым
       <словарь, содержащий атрибуты и их значения>)
"""

def test_method(self): 
    print("This is Test class method!") 
  
# creating a base class  
class Base: 
    def myfun(self): 
        print("This is inherited method!") 

  
# Creating Test class dynamically using type() 
Test = type('Test', (Base, ), dict(x="atul", my_method=test_method)) 
  
# Print type of Test  
print("Type of Test class: ", type(Test))  # Type of Test class:  <class 'type'>
  
# Creating instance of Test class 
test_obj = Test() 
print("Type of test_obj: ", type(test_obj))  # Type of test_obj:  <class '__main__.Test'>
  
# calling inherited method 
test_obj.myfun()                # This is inherited method!
  
# calling Test class method 
test_obj.my_method()            # This is Test class method!
  
# printing variable 
print(test_obj.x)               # atul


"""
После динамического создания можно добавить еще методы """
def test_more(self):
    print('yet another method')

Test.test_more = test_more
print("add metod:",hasattr(Test, 'test_more'))


