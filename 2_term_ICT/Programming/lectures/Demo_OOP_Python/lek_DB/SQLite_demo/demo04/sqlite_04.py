import sqlite3

#con = sqlite3.connect("test.db")
con = sqlite3.connect(":memory:")

cur = con.cursor()

with con:
    cur.execute("""
        CREATE TABLE user (
                        id INT NOT NULL PRIMARY KEY,
                        name TEXT,
                        age INTEGER
                          );
                """)

query = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'
data = [(2, 'Bond', 25),(3, 'Anna', 21),(4, 'Kolya', 19)]

with con:
    cur.executemany(query, data)
    data = (1, "Sasha", 32)

with con:
    cur.execute("INSERT INTO user (id, name, age) values(?, ?, ?)", data)


curdat = cur.execute("SELECT * FROM user WHERE age <= 22")
print(curdat.fetchall())
# [(3, 'Anna', 21), (4, 'Kolya', 19)]

print(cur.execute("SELECT * FROM USER WHERE age <= 22").fetchone())
# (3, 'Anna', 21)

'''Таблица языков '''
with con:
    cur.execute("""
                CREATE TABLE language (
                    id INT NOT NULL PRIMARY KEY,
                    name TEXT
                            );
                """)


'''связующая таблица'''
with con:
    cur.execute("""
            CREATE TABLE user_language (
                    user_id INT,
                    language_id INT,
                    PRIMARY KEY(user_id, language_id),
                    FOREIGN KEY(user_id) REFERENCES user(id),
                    FOREIGN KEY(language_id) REFERENCES language(id)
                                        );
                """)

data = [(1, "english"), (2, "spanish"), (3, "french") ]
with con:
    cur.executemany("INSERT INTO language VALUES(?, ?)", data)

''''обозначим пользователей, которые знают иностранные языки'''
data = [
    (1, 2), # Саша знает испанский
    (2, 1), # Бонд знает английский
    (2, 2), # Бонд еще знает испанский
    (3, 3), # Анна знает французский
    ]

with con:
    cur.executemany("INSERT INTO user_language VALUES(?, ?)", data)


'''Выведем пользователей и языки, которые они знают''' 
dt = cur.execute("""
                SELECT user.name, language.name 
                FROM user, language, user_language
                WHERE (user.id = user_language.user_id AND
                        language.id = user_language.language_id)
                """).fetchall()

print(*dt, sep='\n')

con.close()





