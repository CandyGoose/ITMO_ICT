import sqlite3
import datetime
from sqlite3 import Error

def sql_connection0():
    '''создание базы данных'''
    try:
        con = sqlite3.connect(':memory:')
        #con = sqlite3.connect('mydatabase.db')
        print("Connection is established: Database is created in memory")
    except Error:
        print(Error)
    finally:
        con.close()

#sql_connection0()

        
def sql_connection():
    '''создание базы данных'''
    try:
        con = sqlite3.connect(':memory:')
        #con = sqlite3.connect('mydatabase.db')
    except Error:
        print(Error)    
    else:
        return con
    
      
def sql_table(con):
    '''Создание таблицы'''
    cursorObj = con.cursor()
    cursorObj.execute("""CREATE TABLE if not exists employees( 
        id integer PRIMARY KEY,
        name text,
        salary real,
        department text,
        position text,
        hireDate text)
        """)
    con.commit()

def sql_insert(con, entities):
    '''Вставка данных в таблицу'''
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    con.commit()

def sql_insert_many(con, entities):
    '''Вставка нескольких строк в таблицу'''
    cursorObj = con.cursor()
    cursorObj.executemany('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    con.commit()
    
def sql_fetch(con):
    '''Выборка всех данных'''
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM employees')
    #count = cursorObj.execute('SELECT id, name FROM employees WHERE salary > 800.0')
    #cursorObj.execute('SELECT name from sqlite_master WHERE type = "table" AND name = "employees"') # выборка с проверкой наличия таблицы
    rows = cursorObj.fetchall()
    return rows

def sql_update(con, updatedata):
    '''Обновление данных'''
    cursorObj = con.cursor()
    count = (cursorObj.execute('UPDATE employees SET name = ? where id = ?', updatedata)).rowcount
    con.commit()
    return count

def sql_table2(con):
    cursorObj = con.cursor()
    cursorObj.execute('create table if not exists assignments(id integer, name text, date date)')
    data = [(1, "Ridesharing", datetime.date(2017, 1, 2)), (2, "Water Purifying", datetime.date(2018, 3, 4))]
    cursorObj.executemany("INSERT INTO assignments VALUES(?, ?, ?)", data)
    con.commit()


con = sql_connection()
sql_table(con)
entities = [(2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06'), (3, 'Jonw', 1800, 'Pro', 'Tech', '2019-02-06')]
for i in entities:
    sql_insert(con, i)

entities = [(4, 'Andrew', 80, 'IT', 'Tech', '2020-02-06'), (5, 'Piter', 180, 'Pro', 'Tech', '2020-02-06')]
sql_insert_many(con, entities)

data = sql_fetch(con)
print(data)

k = sql_update(con, ('Rogers',2))
data = sql_fetch(con)
print('Все обновлено:', k, '\nДанные:', data)

sql_table2(con)     # создание новой таблицы
''' Список таблиц'''
cursorObj = con.cursor()
cursorObj.execute('SELECT name from sqlite_master where type= "table"')
print('Таблицы:', cursorObj.fetchall())

'''Удаление таблицы'''
cursorObj = con.cursor()
cursorObj.execute('DROP table if exists employees')
con.commit()

cursorObj.execute('SELECT name from sqlite_master where type= "table"')
print('Таблицы (после удаления):', cursorObj.fetchall())


con.close()


