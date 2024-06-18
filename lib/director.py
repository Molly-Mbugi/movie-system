from config import conn, cursor

class Director:
    def __init__(self, id, name, production):
        self.id = id
        self.name = name
        self.production = production

    @staticmethod
    def create(name, production):
        cursor.execute("INSERT INTO directors (name, production) VALUES (?, ?)", (name, production))
        conn.commit()
        return Director(cursor.lastrowid, name, production)

    @staticmethod
    def find_by_id(id):
        cursor.execute("SELECT * FROM directors WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            return Director(*row)
        return None

    @staticmethod
    def find_by_name(name):
        cursor.execute("SELECT * FROM directors WHERE name LIKE ?", ('%' + name + '%',))
        rows = cursor.fetchall()
        return [Director(*row) for row in rows]

    @staticmethod
    def get_all_directors():
        cursor.execute("SELECT * FROM directors")
        rows = cursor.fetchall()
        return [Director(*row) for row in rows]

    def update(self):
        cursor.execute("UPDATE directors SET name = ?, production = ? WHERE id = ?", (self.name, self.production, self.id))
        conn.commit()

    def delete(self):
        cursor.execute("DELETE FROM directors WHERE id = ?", (self.id,))
        conn.commit()

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Production: {self.production}"


    