import sqlite3

CONN = sqlite3.connect('music.db')
CURSOR = CONN.cursor()

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql)

    def save(self):
        if self.id is None:
            sql = "INSERT INTO songs (name, album) VALUES (?, ?)"
            CURSOR.execute(sql, (self.name, self.album))
            # Retrieve the last inserted row ID and set it as the song's ID
            self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        return song
