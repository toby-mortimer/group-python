import sqlite3
from sqlite3 import Error, connect
from db import DB
from PeopleTable import People


class Records:
    def __init__(self, conn) -> None:
        self.conn = conn

    def create_record(table, conn):
        query = f"INSERT INTO '{table}' ('FirstName', 'Surname') VALUES (?,?)"
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
