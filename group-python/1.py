from db import DB
from PeopleTable import People
from record import Records

database = DB('test.db')
conn = database.Conn
people = People(conn)
