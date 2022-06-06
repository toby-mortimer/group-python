import sqlite3
from sqlite3 import Error, connect
from db import DB
from PeopleTable import People


class Records:
    def __init__(self, conn) -> None:
        self.conn = conn

    def create_record(table, conn):
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor

        cursor.execute(
            "INSERT INTO test VALUES (2, 'firstName', 'lastName', 16)")

        conn.commit()
