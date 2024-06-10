from config import conn, cursor

class Director:
    def __init__(self, id, name, production):
        self.id = id
        self.name = name
        self.production = production

    def __repr__(self):
        return f"<Director {self.id}: {self.name}, {self.production}>"

    @classmethod
    def drop_table(cls):
        """ Drop the directors table if it exists """
        sql = "DROP TABLE IF EXISTS directors"
        cursor.execute(sql)
        conn.commit()