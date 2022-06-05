import sqlite3
from sqlite3 import Error
from db import DB


class People:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self.create_table()

    def create_table(self):
        query = """ 
                "Id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	            "FirstName"	TEXT NOT NULL,
	            "Surname" TEXT NOT NULL,
	            "Age" INTEGER NOT NULL """
        self.cursor.execute(query)
