import sqlite3

''' Получение значения из таблицы '''
db_file = 'database.db'
schema_file = 'schema.sql'

with open(schema_file, 'r') as rf:
    # Read the schema from the file
    schema = rf.read()


with sqlite3.connect(db_file) as conn:
    cursor = conn.cursor()
    cursor.execute(""" select * from images """)
    for row in cursor.fetchall():
        name, size, date = row
        print(f'{name} {size} {date}')

'''
sample.png 100 2019-10-10
ask_python.png 450 2019-05-02
class_room.jpeg 1200 2018-04-07
'''
