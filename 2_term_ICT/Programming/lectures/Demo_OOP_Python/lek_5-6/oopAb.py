# Абстрактный класс (Abstract class).
"""
Простая реализация абстрактного класса в Python —
добавить в базовый класс методы по умолчанию, выбрасывающие исключение NotImplementedError.
"""
class AbstractDocument :
     
    def __init__(self, name):
         
        self.name = name
         
    # Метод невозможно использовать, так как всегда выбрасывает ошибку.
    # Абстрактный метод
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")    
     
     
 
class PDF(AbstractDocument):
    # Переопределить метод родительского класса
    def show(self):
        print ("Show PDF document:", self.name)
         
         
class Word(AbstractDocument):     
     
    def show(self):
        print ("Show Word document:", self.name)
 


documents = [ PDF("Python tutorial"),
              Word("Java IO Tutorial"),
              PDF("Python Date & Time Tutorial") ]     
 
 
for doc in documents :
    doc.show()
    
ab = AbstractDocument("U") # млжно создать экземпляр "абстрактного" класса
ab.show()           # NotImplementedError: Subclass must implement abstract method
