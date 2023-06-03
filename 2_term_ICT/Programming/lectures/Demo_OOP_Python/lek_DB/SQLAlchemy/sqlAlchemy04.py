""" Создание базы данных
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

'''Каждый объект Table является членом коллекции - MetaData,
   этот объект доступен с помощью атрибута metadata декларативного базового класса. 
   Метод MetaData.create_all() передает engine в качестве источника подключения к базе данных. 
   Для всех таблиц, которые еще не были созданы, он выдает операторы CREATE TABLE в базу данных
'''
Base.metadata.create_all(engine)
'''
Выполненяются выражения SQL:
CREATE TABLE customers (
   id INTEGER NOT NULL,
   name VARCHAR,
   address VARCHAR,
   email VARCHAR,
   PRIMARY KEY (id)
)

'''

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

c1 = Customers(name = 'Ravi Kumar', address = 'Station Road Nanded', email = 'ravi@gmail.com')
'''Добавление записи в таблицу клиентов'''
session.add(c1)
session.commit()

'''Чтобы добавить несколько записей, мы можем использовать метод add_all () класса сеанса'''
session.add_all([
   Customers(name = 'Komal Pande', address = 'Koti, Hyderabad', email = 'komal@gmail.com'), 
   Customers(name = 'Rajender Nath', address = 'Sector 40, Gurgaon', email = 'nath@gmail.com'), 
   Customers(name = 'S.M.Krishna', address = 'Budhwar Peth, Pune', email = 'smk@gmail.com')]
)

session.commit()
