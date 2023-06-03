"""
Установка пакета
pip install sqlalchemy
"""
import sqlalchemy as db
from sqlalchemy import Column, Integer, String

engine = db.create_engine('sqlite:///college3.db', echo = True)
'''для создания базового класса используется функция declarative_base()
   определена в модуле sqlalchemy.ext.declarative'''
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


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

class Students(Base):
   __tablename__ = 'students'
   id = Column(Integer, primary_key =  True)
   name = Column(String)
   lastname = Column(String)
   


result = session.query(Students).all()
result = session.query(Students).filter(Students.id>5)
result = session.query(Students).filter(Students.name=='Mari')


