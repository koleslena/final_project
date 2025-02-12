import sqlite3 
from sqlite3 import OperationalError

def get_connection():
    """Создает соединение с базой данных."""
    return sqlite3.connect('students.db')

def initialize_database(filename):
    
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    sqlCommands = sqlFile.split(';')

    conn = get_connection()
    cursor = conn.cursor()

    for command in sqlCommands:
        try:
            cursor.execute(command)
        except OperationalError as err:
            print(f"Command skipped: {command}, {err}")

