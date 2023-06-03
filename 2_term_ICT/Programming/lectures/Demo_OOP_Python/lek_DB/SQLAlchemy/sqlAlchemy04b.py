""" Выполнение запросов
Установка пакета
pip install sqlalchemy
"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///sales.db', echo = True)
'''для создания базового класса используется функция declarative_base()
   определена в модуле sqlalchemy.ext.declarative'''
Base = declarative_base()

'''класс Заказчик содержит таблицу для сопоставления,
   а также имена и типы данных столбцов в ней'''
class Customers(Base):
   __tablename__ = 'customers'
   id = Column(Integer, primary_key = True)
   name = Column(String)
   address = Column(String)
   email = Column(String)

'''
Чтобы взаимодействовать с базой данных, нужно получить ее дескриптор.
Объект сеанса является дескриптором базы данных.
Класс сеанса определяется с помощью sessionmaker() — настраиваемого метода фабрики сеансов,
который привязан к объекту, созданному ранее.
'''
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)

'''объект сеанса устанавливается с помощью конструктора '''
session = Session()

'''метод all() возвращает набор результатов в виде списка объектов'''
result = session.query(Customers).all()

for row in result:
   print ("Name:",row.name, "Address:",row.address, "Email:",row.email)

'''
Чтобы изменить данные определенного атрибута любого объекта:
- присвоить ему новое значение
- зафиксировать изменения, чтобы сделать это изменение постоянным. 
'''
'''Извлечение данных по ID:'''
x = session.query(Customers).get(2)
print ("ID:", x.id, "Name:", x.name, "Address:", x.address, "Email:", x.email)
'''Обновим поле Address, назначив новое значение:''' 
x.address = 'Banjara Hills'
session.commit()
#session.rollback() # отмена изменения - откат к прежнему значению
'''Проверка обновления'''
x = session.query(Customers).get(2)
print ("ID:", x.id, "Name:", x.name, "Address:", x.address, "Email:", x.email)

'''для извлечения объекта, соответствующему первой строке таблицы - метод first()''' 
x = session.query(Customers).first()
print ("ID:", x.id, "Name:", x.name, "Address:", x.address, "Email:", x.email)

'''Для массовых обновлений - метод update() объекта Query. 
Дать префикс «мистер» имя в каждой строке (кроме ID = 2)'''
session.query(Customers).filter(Customers.id!= 2).update({Customers.name:"Mr."+Customers.name}, synchronize_session = False)
session.commit()
result = session.query(Customers).all()
for row in result:
   print ("Name:",row.name, "Address:",row.address, "Email:",row.email)

'''Фильтр'''
result = session.query(Customers).filter(Customers.id%2==0)
for row in result:
   print ("ID:", row.id, "Name: ",row.name, "Address:",row.address, "Email:",row.email)

'''метод like () создает критерии LIKE для предложения WHERE в выражении SELECT'''
result = session.query(Customers).filter(Customers.name.like('%Ra%'))
for row in result:
   print ("ID:", row.id, "Name: ",row.name, "Address:",row.address, "Email:",row.email)

'''соединение создается
   - путем помещения нескольких критериев, разделенных запятыми в фильтре
   - или использования метода and_() ''' 
result = session.query(Customers).filter(Customers.id>2, Customers.name.like('%Ra%'))
for row in result:
   print ("ID:", row.id, "Name: ",row.name, "Address:",row.address, "Email:",row.email)

''' Оператор in проверяет, принадлежит ли значение столбца к коллекции элементов в списке.
    Это обеспечивается методом in_ ()'''
result = session.query(Customers).filter(Customers.id.in_([1,3]))
for row in result:
   print ("ID:", row.id, "Name: ",row.name, "Address:",row.address, "Email:",row.email)

''' методы and_ и or_ ()'''
from sqlalchemy import and_
result = session.query(Customers).filter(and_(Customers.id>2, Customers.name.like('%Ra%')))
for row in result:
   print ("ID:", row.id, "Name: ",row.name, "Address:",row.address, "Email:",row.email)

from sqlalchemy import or_
result = session.query(Customers).filter(or_(Customers.id>2, Customers.name.like('%Ra%')))
for row in result:
   print ("ID:", row.id, "Name: ",row.name, "Address:",row.address, "Email:",row.email)


