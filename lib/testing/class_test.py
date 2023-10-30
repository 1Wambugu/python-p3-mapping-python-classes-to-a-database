# lib/testing/class_test.py
from lib.song import Song
import time

class TestClass:
    '''Class Song in song.py'''

    def test_creates_songs_table(self, db_connection):
        '''has classmethod "create_table()" that creates a table "songs" if the table does not exist.'''
        conn, cursor = db_connection
        cursor.execute('''DROP TABLE IF EXISTS songs''')
        # Add a delay to avoid race conditions
        time.sleep(1)
        Song.create_table()
        assert cursor.execute("SELECT * FROM songs") is not None

    def test_initializes_with_name_and_album(self):
        '''takes a name and album as __init__ arguments and saves them as instance attributes.'''
        song = Song("Hold On", "Born to Sing")
        assert song.name == "Hold On" and song.album == "Born to Sing"

    def test_saves_song_to_table(self, db_connection):
        '''has instancemethod "save()" that saves a song to music.db.'''
        conn, cursor = db_connection
        cursor.execute('''DROP TABLE IF EXISTS songs''')
        # Add a delay to avoid race conditions
        time.sleep(1)
        Song.create_table()

        song = Song("Hold On", "Born to Sing")
        song.save()
        db_song = cursor.execute(
            'SELECT * FROM songs WHERE name=? AND album=?',
            ('Hold On', 'Born to Sing')
        ).fetchone()
        assert db_song is not None, "Song was not saved to the table."

    def test_creates_and_returns_song(self, db_connection):
        '''has classmethod "create()" that creates a Song instance, saves it, and returns it.'''
        conn, cursor = db_connection
        cursor.execute('''DROP TABLE IF EXISTS songs''')
        # Add a delay to avoid race conditions
        time.sleep(1)
        Song.create_table()

        song = Song.create("Hold On", "Born to Sing")
        db_song = cursor.execute(
            'SELECT * FROM songs WHERE name=? AND album=?',
            ('Hold On', 'Born to Sing')
        ).fetchone()
        assert db_song[0] == song.id and db_song[1] == song.name and db_song[2] == song.album
