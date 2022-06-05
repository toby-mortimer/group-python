import sqlite3
from sqlite3 import Error, connect
from db import DB
from PeopleTable import People


class Records:
    def __init__(self, conn) -> None:
        self.conn = conn

    def create_record(table, conn):
        cursor = conn.cursor()
        query = """ INSERT INTO table 
                ('Id' 'FirstName', 'Surname' 'Age') 
                VALUES 
                (1, 'Toby' , 'Mortimer' , 16 ) """
        cursor.execute(query)
        conn.commit()
