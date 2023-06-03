"""
pip install sqlalchemy
"""
import sqlalchemy as db

engine = db.create_engine('sqlite:///college3.db', echo = True)

connection = engine.connect()

''' объект класса MetaData из метаданных SQLAlchemy представляет собой коллекцию объектов Table
    и связанных с ними конструкций схемы '''
metadata = db.MetaData()

studentsTable = db.Table('students', metadata, autoload=True, autoload_with=engine)

print('Print the column names: ', studentsTable.columns.keys())
print('Print full table metadata: ', repr(metadata.tables['students']))

#query0 = 'SELECT * FROM students'
query0 = db.select([studentsTable])

'''result - объект, возвращаемый методом execute(),
   его можно использовать различными способами для получения данных,
   возвращаемых запросом '''
result = connection.execute(query0)

'''resultSet - фактические данные, запрашиваемые в запросе при использовании
   метода выборки, такого как .fetchall() '''
resultSet = result.fetchall()
print(*resultSet, sep='\n')   # вывод распаковкой из списка

'''Примеры запросов'''
#where
query = "SELECT * FROM students WHERE name == 'Mari'"
#query = db.select([studentsTable]).where(studentsTable.columns.name == 'Mari')
result = connection.execute(query)
resultSet = result.fetchall()
print(*resultSet, sep='\n')   # вывод распаковкой из списка

#and, or, not
query = "SELECT * FROM students WHERE name == 'Mari' AND NOT id > 20"
#query = db.select([studentsTable]).where(db.and_(studentsTable.columns.name == 'Mari', studentsTable.columns.id < 20))
result = connection.execute(query)
resultSet = result.fetchall()
print(*resultSet, sep='\n')   # вывод распаковкой из списка

#order by
query = "SELECT * FROM students ORDER BY name DESC, id"
#query = db.select([studentsTable]).order_by(db.desc(studentsTable.columns.name), studentsTable.columns.id)
result = connection.execute(query)
resultSet = result.fetchall()
print(*resultSet, sep='\n')   # вывод распаковкой из списка

#functions
query = "SELECT COUNT(name)"
#query = db.select([db.func.count(studentsTable.columns.name)])
result = connection.execute(query).scalar() # результат содержит только одно значение
print("Count - ", result)



'''Можно использовать fetchmany()  для задания оптимального количество строк
(преодоление проблем с памятью в случае больших наборов данных) '''
result = connection.execute(query0)
flag = True
while flag:
    partial_results = result.fetchmany(10)
    if(partial_results == []):
       flag = False
    print('part', partial_results)
   
''' Преобразовать в датафрейм '''
import pandas as pd
df = pd.DataFrame(resultSet)
df.columns = resultSet[0].keys()
print(df.columns)
