from config import conn, cursor

class Director:
    def __init__(self, name, production):
        self.name = name
        self.production = production

    def __repr__(self):
        return f"<Director {self.name}: {self.production}>"

    @classmethod
    def create_table(cls):
        """ Create the directors table if it does not exist """
        sql = """
            CREATE TABLE IF NOT EXISTS directors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                production TEXT
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the directors table if it exists """
        sql = "DROP TABLE IF EXISTS directors"
        cursor.execute(sql)
        conn.commit()

    def save(self):
        sql = """
            INSERT INTO directors (name, production)
            VALUES (?, ?)
        """
        cursor.execute(sql, (self.name, self.production))
        conn.commit()

        self.id = cursor.lastrowid

    