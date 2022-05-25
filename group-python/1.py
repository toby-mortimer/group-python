from db import DB
from PeopleTable import People

database = People('test.db')

conn = database.Conn

conn.execute('SELECT * FROM People')
c = conn.cursor()
data = c.fetchall()

print(data)
