"""
Установка пакета
pip install sqlalchemy
"""
from sqlalchemy import create_engine

''' Для создания базы данных sqlite '''
engine = create_engine('sqlite:///college3.db', echo = True) # Флаг echo — ярлык для настройки ведения журнала SQLAlchemy (консоль будет отображать фактический запрос SQL для создания таблицы )

from sqlalchemy import Table, Column, Integer, String, MetaData

''' объект класса MetaData из метаданных SQLAlchemy представляет собой коллекцию объектов Table
и связанных с ними конструкций схемы '''
meta = MetaData()

''' Объект класса Table представляет соответствующую таблицу в базе данных
Объект столбца представляет столбец в таблице базы данных.
Конструктор принимает имя, тип и другие параметры, такие как primary_key, автоинкремент и другие ограничения
'''
students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)

'''
Функция create_all() использует объект engine для создания всех определенных
объектов таблицы и сохраняет информацию в метаданных
'''
meta.create_all(engine)

print('Print the column names: ', students.columns.keys())
print('Print full table metadata: ', repr(meta.tables['students']))

'''оператор INSERT создается путем выполнения метода insert() '''
ins = students.insert()
'''Можно вставить значение в определенное поле с помощью метода values() для вставки объекта'''
ins = students.insert().values(name = 'Mari', lastname = 'Fapoor')

'''
Чтобы выполнить результирующие выражения SQL, требуется получить объект соединения,
представляющий активно извлеченный ресурс соединения DBAPI, а затем передать объект выражения
'''
conn = engine.connect()
result = conn.execute(ins)

'''
Чтобы вставить несколько записей данных - используется метод executemany() в DBAPI,
здесь можно отправить список словарей, каждый из которых содержит отдельный набор параметров для вставки
'''
conn.execute(students.insert(), [
   {'name':'Ra', 'lastname' : 'Kanna'},
   {'name':'Kogal','lastname' : 'Bhandari'},
   {'name':'Pol','lastname' : 'Sattar'},
   {'name':'Lisa','lastname' : 'Rahans'},
])


''' Метод select() табличного объекта позволяет создавать выражение SELECT '''
s = students.select()
conn = engine.connect()
result = conn.execute(s)

'''Результирующая переменная является эквивалентом курсора в DBAPI.
Теперь можем получать записи, используя метод fetchone()'''
row = result.fetchone()
print('fetchone:', row)

print('Все выбранные строки в таблице:')
for row in result:
   print (row)


'''Предложение WHERE запроса SELECT может быть применено с помощью Select.where()'''
p = 2
s = students.select().where(students.c.id > p)
result = conn.execute(s)

print('отображать строки с идентификатором > 2')
for row in result:
   print (row)

'''Конструкция text() используется для составления текстового оператора,
который в основном передается в базу данных без изменений. 
Он создает новое TextClause, представляющее текстовую строку SQL напрямую ''' 
from sqlalchemy import text
t = text("SELECT * FROM students")
result = conn.execute(t)

'''используются связанные параметры в текстовом SQL''' 
s = text("select students.name, students.lastname from students where students.name between :x and :y")
conn.execute(s, x = 'A', y = 'L').fetchall()


