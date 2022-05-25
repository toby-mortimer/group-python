from db import DB
from PeopleTable import People


def __init__(self, conn, query):
    database = DB('test.db')
    conn = database.Conn
    people = People(query)

    conn.execute('SELECT * FROM People')
    cursor = conn.cursor()
    data = cursor.fetchall()

    print(data)
