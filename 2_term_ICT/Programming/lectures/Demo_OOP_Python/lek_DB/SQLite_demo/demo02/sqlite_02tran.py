import sqlite3

''' Управление транзакциями '''

db_filename = 'database.db'

def display_table(conn):
    cursor = conn.cursor()
    cursor.execute('select name, size, date from images;')
    for name, size, date in cursor.fetchall():
        print(name, size, date)


with sqlite3.connect(db_filename) as conn1:
    print('Before changes:')
    display_table(conn1)

    cursor1 = conn1.cursor()
    cursor1.execute("""
insert into images (name, size, date) values ('JournalDev.png', 2000, '2020-02-20'); """
                    )
    print('\nAfter changes in conn1:')
    display_table(conn1)

    print('\nBefore commit:')
    with sqlite3.connect(db_filename) as conn2:
        display_table(conn2)

    # Commit from the first connection
    conn1.commit()
    print('\nAfter commit:')
    with sqlite3.connect(db_filename) as conn3:
        display_table(conn3)

    cursor1.execute(
                """ insert into images (name, size, date) values ('Hello.png', 200, '2020-01-18'); """
                )
    print('\nBefore commit:')
    with sqlite3.connect(db_filename) as conn2:
        display_table(conn2)

    # Revert to changes before conn1's commit
    conn1.rollback()
    print('\nAfter connection 1 rollback:')
    with sqlite3.connect(db_filename) as conn4:
        display_table(conn4)


'''удаление для реализации повторного запуска (добавления данных)'''

with sqlite3.connect(db_filename) as conn5:
    cursor5 = conn5.cursor()
    cursor5.execute("""delete from images where name='JournalDev.png'; """                    )
    conn5.commit()
    print('\nAfter delete in conn5:')
    display_table(conn5)

