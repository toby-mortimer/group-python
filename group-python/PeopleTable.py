import sqlite3
from sqlite3 import Error
from db import DB


class People:
    def __init__(self) -> None:
        pass
    conn = ('test.db')
    curs = conn.cursor()
    curs.execute()

    table = """ CREATE TABLE "People" (
            "Int"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            "FirstName"	TEXT NOT NULL,
            "Surname"	TEXT NOT NULL
            ); """

    curs.execute(table)
