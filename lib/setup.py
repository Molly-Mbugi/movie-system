from config import conn, cursor

def create_tables():
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
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS directors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            production TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Call the function to create the tables
create_tables()

