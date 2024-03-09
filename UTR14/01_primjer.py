# 1. Modelirajte bazu podataka o studentima koja sadrži sljedeće podatke:
# - ime studenta
# - prezime studenta
# - datum rođenja studenta
# - adresa studenta
# - ime mentora
# - prezime mentora
# - adresa mentora
# - ime zamjenika mentora
# - prezime zamjenika mentora
# - adresa zamjenika mentora

import sqlite3 
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_mentors(conn):
     query = 'INSERT INTO mentors VALUES(oib, ime, prezime, adresa)'
     data = ()

database = 'UTR14/orsus_database.db'

sql_create_students_table = "CREATE TABLE IF NOT EXISTS students (oib INTEGER PRIMARY KEY, ime TEXT NOT NULL, prezime TEXT NOT NULL, datum_rođenja TEXT NOT NULL, adresa TEXT NOT NULL);"

sql_create_mentors_table = "CREATE TABLE IF NOT EXISTS mentors (oib INTEGER PRIMARY KEY, ime TEXT NOT NULL, prezime TEXT NOT NULL, adresa TEXT NOT NULL);"

sql_create_groups_table = "CREATE TABLE IF NOT EXISTS groups(id integer PRIMARY KEY AUTOINCREMENT, naziv TEXT, voditelj_grupe TEXT,zamjenik_grupe TEXT);"

conn = create_connection(database)

if conn is not None:
    create_table(conn, sql_create_students_table)
    create_table(conn, sql_create_mentors_table)
    create_table(conn, sql_create_groups_table)

else:
    print("Error! cannot create the database connection.")