from lib.db import CURSOR, CONN

class Movie:

    def __init__(self, id=None, title=None, about=None, genre=None, duration=None, release=None, director_id=None):
        self.id = id
        self.title = title
        self.about = about
        self.genre = genre
        self.duration = duration
        self.release = release
        self.director_id = director_id

    def __repr__(self):
        return f"<Movie {self.id}: {self.title}, {self.about}, {self.genre}, {self.duration}, {self.release}, Director ID: {self.director_id}>"
