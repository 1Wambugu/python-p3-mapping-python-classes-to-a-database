# lib/config.py
import sqlite3
import os

def initialize_database(testing=False):
    if testing:
        conn = sqlite3.connect(':memory:')
    else:
        conn = sqlite3.connect('music.db', check_same_thread=False)
    cursor = conn.cursor()
    return conn, cursor

def close_database(conn):
    conn.close()

CONN, CURSOR = initialize_database(os.environ.get("PYTEST_CURRENT_TEST"))
