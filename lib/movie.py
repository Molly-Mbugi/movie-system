from config import conn, cursor

class Movie:
    def __init__(self, id, title, genre, about, duration, release_date, director_id):
        self.id = id
        self.title = title
        self.genre = genre
        self.about = about
        self.duration = duration
        self.release_date = release_date
        self.director_id = director_id

    @staticmethod
    def create(title, genre, about, duration, release_date, director_id):
        cursor.execute("INSERT INTO movies (title, genre, about, duration, release_date, director_id) VALUES (?, ?, ?, ?, ?, ?)",
                       (title, genre, about, duration, release_date, director_id))
        conn.commit()
        return Movie(cursor.lastrowid, title, genre, about, duration, release_date, director_id)

    @staticmethod
    def find_by_id(id):
        cursor.execute("SELECT * FROM movies WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            return Movie(*row)
        return None

    @staticmethod
    def find_by_name(name):
        cursor.execute("SELECT * FROM movies WHERE title LIKE ?", ('%' + name + '%',))
        rows = cursor.fetchall()
        return [Movie(*row) for row in rows]

    @staticmethod
    def get_all_movies():
        cursor.execute("SELECT * FROM movies")
        rows = cursor.fetchall()
        return [Movie(*row) for row in rows]

    def update(self):
        cursor.execute("UPDATE movies SET title = ?, genre = ?, about = ?, duration = ?, release_date = ?, director_id = ? WHERE id = ?",
                       (self.title, self.genre, self.about, self.duration, self.release_date, self.director_id, self.id))
        conn.commit()

    def delete(self):
        cursor.execute("DELETE FROM movies WHERE id = ?", (self.id,))
        conn.commit()

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Genre: {self.genre}, Duration: {self.duration} minutes, Release Date: {self.release_date}, Director ID: {self.director_id}"

