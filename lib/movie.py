from config import conn, cursor

class Movie:
    def __init__(self, id, title, about, genre, duration, release):
        self.id = id
        self.title = title
        self.about = about
        self.genre = genre
        self.duration = duration
        self.release = release

    def __repr__(self):
        return f"<Movie {self.id}: {self.title}, {self.about}, {self.genre}, {self.duration}, {self.release}>"
