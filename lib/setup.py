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

    conn.commit()
    conn.close()

# Call the function to create the table
create_movies_table()
