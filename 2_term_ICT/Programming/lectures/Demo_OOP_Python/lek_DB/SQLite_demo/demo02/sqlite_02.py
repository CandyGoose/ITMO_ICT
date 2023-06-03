import sqlite3
import os

'''
Полезно проверить, существует ли уже файл в системе
'''
def check_db(filename):
    return os.path.exists(filename)

''' создадим соединение с базой данных Python SQLite '''
db_file = 'database.db'
schema_file = 'schema.sql'

if check_db(db_file):
    print('Database already exists. Exiting...')
    exit(0)

with open(schema_file, 'r') as rf:
    # Read the schema from the file
    schema = rf.read()


with sqlite3.connect(db_file) as conn:
    print('Created the connection!')
    # Execute the SQL query to create the table
    conn.executescript(schema)
    print('Created the Table! Now inserting')
    conn.executescript("""insert into images (name, size, date) values ('sample.png', 100, '2019-10-10'), ('ask_python.png', 450, '2019-05-02'), ('class_room.jpeg', 1200, '2018-04-07'); """)
    print('Inserted values into the table!')


print('Automatically closed the connection!')


