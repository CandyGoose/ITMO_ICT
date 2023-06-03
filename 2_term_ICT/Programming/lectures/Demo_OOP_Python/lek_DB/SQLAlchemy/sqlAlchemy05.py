""" Отношения -
    создается таблица счетов, которая может содержать любое количество счетов,
    принадлежащих клиенту - отношения один ко многим

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

'''Теперь, когда создаем объект Customer, будет представлена пустая коллекция счетов в форме списка '''
c1 = Customer(name = "Gopal Krishna", address = "Bank Street Hydarebad", email = "gk@gmail.com")
'''можем назначить элементы в списке''' 
c1.invoices = [Invoice(invno = 10, amount = 15000), Invoice(invno = 14, amount = 3850)]

'''передадим новый объект в базу данных, используя Session''' 
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
session.add(c1)
session.commit()

'''Это автоматически сгенерирует запросы INSERT для таблиц клиентов и счетов 
INSERT INTO customers (name, address, email) VALUES (?, ?, ?) 
('Gopal Krishna', 'Bank Street Hydarebad', 'gk@gmail.com')
INSERT INTO invoices (custid, invno, amount) VALUES (?, ?, ?)
(2, 10, 15000)
INSERT INTO invoices (custid, invno, amount) VALUES (?, ?, ?)
(2, 14, 3850)
'''

'''Вариант 1. Можно создать объект Customer, предоставив сопоставленный атрибут счетов в самом конструкторе''' 
c2 = Customer(
      name = "Govind Pant", 
      address = "Gulmandi Aurangabad", 
      email = "gpant@gmail.com", 
      invoices = [Invoice(invno = 3, amount = 10000), Invoice(invno = 4, amount = 5000)])

#session.add(c2)        # при создании базы - добавить объект с2 
#session.commit()

'''Вариант 2. Список объектов, которые будут добавлены с использованием функции add_all() объекта сеанса''' 
rows = [
   Customer(
      name = "Govind Kala", 
      address = "Gulmandi Aurangabad", 
      email = "kala@gmail.com", 
      invoices = [Invoice(invno = 7, amount = 12000), Invoice(invno = 8, amount = 18500)]),

   Customer(
      name = "Abdul Rahman", 
      address = "Rohtak", 
      email = "abdulr@gmail.com",
      invoices = [Invoice(invno = 9, amount = 15000), 
      Invoice(invno = 11, amount = 6000)
   ])
]

session.add_all(rows)
session.commit()

'''Запросы к таблицам
1) простое неявное соединение между Customer и Invoice
'''
for c, i in session.query(Customer, Invoice).filter(Customer.id == Invoice.custid).all():
   print ("ID: {} Name: {} Invoice No: {} Amount: {}".format(c.id,c.name, i.invno, i.amount))

'''
2) SQL JOIN '''
result = session.query(Customer).join(Invoice).filter(Invoice.amount == 8500).all()

for row in result:
   for inv in row.invoices:
      print (row.id, row.name, inv.invno, inv.amount)

'''Операторы отношений '''
s = session.query(Customer).filter(Invoice.invno.__eq__(12))
s = session.query(Customer).filter(Invoice.custid.__ne__(2))
s = session.query(Invoice).filter(Invoice.invno.contains([3,4,5]))
s = session.query(Customer).filter(Customer.invoices.any(Invoice.invno==11))


'''Загрузка связанных данных
1. Загрузка подзапроса
'''
from sqlalchemy.orm import subqueryload
'''Опция orm.subqueryload() дает второй оператор SELECT, который полностью загружает коллекции,
связанные с только что загруженными результатами'''
c1 = session.query(Customer).options(subqueryload(Customer.invoices)).filter_by(name = 'Govind Pant').one()

''' доступ к данным из двух таблиц ''' 
print (c1.name, c1.address, c1.email)
for x in c1.invoices:
   print ("Invoice no : {}, Amount : {}".format(x.invno, x.amount))

'''
2. Объединенная загрузка
orm.joinedload() - ведущий объект, а также связанный объект или коллекция загружаются за один шаг'''
from sqlalchemy.orm import joinedload
c1 = session.query(Customer).options(joinedload(Customer.invoices)).filter_by(name='Govind Pant').one()

print (c1.name, c1.address, c1.email)
for x in c1.invoices:
   print ("Invoice no : {}, Amount : {}".format(x.invno, x.amount))










