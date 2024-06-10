from config import conn, cursor

class Director:
    def __init__(self, id, name, production):
        self.id = id
        self.name = name
        self.production = production

    def __repr__(self):
        return f"<Director {self.id}: {self.name}, {self.production}>"
