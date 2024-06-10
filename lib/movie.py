from config import conn, cursor

class Movie:
    def __init__(self, title, about, genre, duration, release):
        self.title = title
        self.about = about
        self.genre = genre
        self.duration = duration
        self.release = release

    def __repr__(self):
        return f"<Movie {self.title}: {self.about}, {self.genre}, {self.duration}, {self.release}>"

    @classmethod
    def create_table(cls):
        """ Create the movies table if it does not exist """
        sql = """
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                about TEXT,
                genre TEXT,
                duration INTEGER,
                release_date TEXT
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the movies table if it exists """
        sql = "DROP TABLE IF EXISTS movies"
        cursor.execute(sql)
        conn.commit()

    def save(self):
        sql = """
            INSERT INTO movies (title, about, genre, duration, release_date)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.title, self.about, self.genre, self.duration, self.release))
        conn.commit()

        self.id = cursor.lastrowid
