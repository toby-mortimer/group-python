import sqlite3
from sqlite3 import Error
from db import DB


class People:
    def __init__(self, conn, query):
        self.conn = conn
        self.cursor = conn.cursor()
        self.create_table(query)

    def create_table(self, query):
        query = """ CREATE TABLE IF NOT EXISTS "People" (
                "Id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                "FirstName"	TEXT NOT NULL,
                "Surname"	TEXT NOT NULL
                ); """
        self.cursor.execute(query)
