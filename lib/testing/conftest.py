# conftest.py
import pytest
from lib.config import initialize_database, close_database

@pytest.fixture(scope='function')
def db_connection():
    conn, cursor = initialize_database()
    yield conn, cursor
    close_database(conn)
