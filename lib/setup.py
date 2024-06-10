from config import conn, cursor

def create_movies_table():
    # Create table for movies
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            about TEXT,
            genre TEXT,
            duration INTEGER,
            release_date TEXT
        )
    ''')

def create_directors_table():
    # Create table for directors
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS directors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            production TEXT
        )
    ''')

def create_tables():
    create_movies_table()
    create_directors_table()
    conn.commit()
    conn.close()

# Call the function to create the tables
create_tables()

