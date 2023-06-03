"""
Установка пакета
pip install peewee

Используется открытая тестовая база данных “Chinook”:
github.com/lerocha/chinook-database/blob/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite
"""
from peewee import *

# Создаем соединение с базой данных
conn = SqliteDatabase('Chinook_Sqlite.sqlite')

# Определяем базовую модель от которой будут наследоваться остальные
class BaseModel(Model):
    class Meta:
        database = conn  # соединение с базой

# Определяем модель исполнителя
class Artist(BaseModel):
    artist_id = AutoField(column_name='ArtistId')
    name = TextField(column_name='Name', null=True)

    class Meta:
        table_name = 'Artist'

def print_last_five_artists():
    """ Печатаем последние 5 записей в таблице исполнителей"""
    print('#######################################################')
    cur_query = Artist.select().limit(5).order_by(Artist.artist_id.desc())
    for item in cur_query.dicts().execute():
        print('artist: ', item)

'''Получение одиночной записи с методом модели Model.get()'''
artist = Artist.get(Artist.artist_id == 1)
print('artist: ', artist.artist_id, artist.name)


'''Получение набора записей через нашу модель Model.select()'''
query = Artist.select()
print(query)

query = Artist.select().where(Artist.artist_id < 10).limit(5).order_by(Artist.artist_id.desc())
print(query)

artists_selected = query.dicts().execute()
print(artists_selected)   # итератор по полученным из базы записям

'''каждая итерация соответствует одной строке таблицы и соответственно одному исполнителю'''
for artist in artists_selected:
    print('artist: ', artist)   # artist:  {'artist_id': 9, 'name': 'BackBeat'}


'''Создание записи

Первый способ: Model.create() — передаем все требуемые параметры сразу'''
Artist.create(name='1-Qwerty')

'''Второй способ: создаем объект класса модели, работаем в коде в содержимым его полей,
а в конце вызываем его метод .save()'''
artist = Artist(name='2-asdfg')
'''Обратите внимание, что здесь метод вызываем у объекта класса модели, а не у самой модели, как в первом способе'''
artist.save()

'''Третий способ — массовое добавление из коллекции методом модели Model.insert_many()
Обратите внимание, что первые два метода не требуют добавления .execute(), а этот требует!'''
artists_data = [{'name': '3-qaswed'}, {'name': '4-yhnbgt'}]
Artist.insert_many(artists_data).execute()

'''Визуализируем последние 5 записей в таблице исполнителей, чтобы убедится, что три примера выше доавили нам 4 новые записи:'''
print_last_five_artists() 

'''Обновление записей

Первый способ обновления записей'''

artist = Artist(name='2-asdfg+++++')
artist.artist_id = 277  # Тот самый первичный ключ, который связывает объект с конкретной строке таблицы базы данных
artist.save()

print_last_five_artists() 

'''Для обновления многих записей сразу, можно испольщовать метод модели Model.update(),
в котором указываем что именно у нас меняется, а метод .where() определяет по каким критериям отбираются записи для изменения'''
query = Artist.update(name=Artist.name + '!!!').where(Artist.artist_id > 275)
query.execute()

print_last_five_artists() 

'''Удаление записей

Первый способ удаления записи — это получение объекта записи методом Model.get() и вызова метода удаления этой записи .delete_instance()'''
artist = Artist.get(Artist.artist_id == 279)
artist.delete_instance()

print_last_five_artists() 

'''Второй способ. Для удаления набора строк можно использовать Model.delete() метод'''
query = Artist.delete().where(Artist.artist_id > 275)
query.execute()

print_last_five_artists() 







# Создаем курсор - специальный объект для запросов и получения данных с базы
cursor = conn.cursor()

# Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
# Получаем результат сделанного запроса
results = cursor.fetchall()
print(results)   # [('A Cor Do Som',), ('AC/DC',), ('Aaron Copland & London Symphony Orchestra',)]




# закрыть соединение с базой данных
conn.close()

