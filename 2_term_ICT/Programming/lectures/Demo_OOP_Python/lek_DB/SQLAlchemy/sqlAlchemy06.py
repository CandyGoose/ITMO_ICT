""" Удаление -
    В базе данных sales.db классы Customer и Invoice сопоставляются с таблицами customer и invoice
    с типом взаимосвязи один-ко-многим. 
    Задача: удалить объект Customer
pip install sqlalchemy
"""
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///sales.db', echo = True)
Base = declarative_base()

'''класс Клиент содержит таблицу для сопоставления,
   а также имена и типы данных столбцов в ней'''
class Customer(Base):
   __tablename__ = 'customers'
   id = Column(Integer, primary_key = True)
   name = Column(String)
   address = Column(String)
   email = Column(String)

'''класс Счет содержит таблицу для сопоставления,
   а также имена и типы данных столбцов в ней
   и указание связи с клиентом

   Отношение «один ко многим» относится к родителю с помощью
   внешнего ключа на дочерней таблице
   '''
class Invoice(Base):
   __tablename__ = 'invoices'
   id = Column(Integer, primary_key = True)
   custid = Column(Integer, ForeignKey('customers.id'))
   invno = Column(Integer)
   amount = Column(Integer)
   customer = relationship("Customer", back_populates = "invoices")

'''Будет сгенерирован запрос CREATE TABLE на SQLite: 
CREATE TABLE invoices (
   id INTEGER NOT NULL,
   custid INTEGER,
   invno INTEGER,
   amount INTEGER,
   PRIMARY KEY (id),
   FOREIGN KEY(custid) REFERENCES customers (id)
)
'''

'''связывается Клиент с классов Счет'''
Customer.invoices = relationship("Invoice", order_by = Invoice.id, back_populates = "customer")

Base.metadata.create_all(engine)

'''настраиваем сеанс и получаем объект Customer,
   запрашивая его с помощью основного идентификатора''' 
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
x = session.query(Customer).get(2)

'''Учитывая, что x.name — это Gopal Krishna удалим этот x из сеанса и посчитаем вхождение этого имени'''
session.delete(x)
k = session.query(Customer).filter_by(name = 'Gopal Krishna').count() # результат проверки
print("Осталось?", k)
'''связанные объекты Invoice для x остались в таблице''' 
k = session.query(Invoice).filter(Invoice.invno.in_([10,14])).count()
print("Осталось?", k)
# 10 и 14 — номера счетов, принадлежащих клиенту.
# Результат запроса должен показать, что связанные объекты не были удалены. 

'''По умолчанию каскадного удаления нет'''

for c, i in session.query(Customer, Invoice).filter(Customer.id == Invoice.custid).all():
   print ("ID: {} Name: {} Invoice No: {} Amount: {}".format(c.id,c.name, i.invno, i.amount))







