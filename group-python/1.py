from db import DB
from PeopleTable import People

database = DB('test.db')
conn = database.Conn
people = People(conn)
