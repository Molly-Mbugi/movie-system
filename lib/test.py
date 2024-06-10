from config import conn, cursor
from movie import Movie
from director import Director

def test_movie_operations():
    # Drop the movies table if it exists
    Movie.drop_table()

    # Create the movies table
    Movie.create_table()

    # Create instances of Movie and save them
    movie1 = Movie(title="The Shawshank Redemption", about="Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.", genre="Drama", duration=142, release="1994-09-23")
    movie1.save()

    movie2 = Movie(title="The Godfather", about="The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.", genre="Crime", duration=175, release="1972-03-24")
    movie2.save()

    # Fetch all movies and print them
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    print("Movies:")
    for movie in movies:
        print(movie)

def test_director_operations():
    # Drop the directors table if it exists
    Director.drop_table()

    # Create the directors table
    Director.create_table()

    # Create instances of Director and save them
    director1 = Director(name="Quentin Tarantino", production="Pulp Fiction")
    director1.save()

    director2 = Director(name="Christopher Nolan", production="Inception")
    director2.save()

    # Fetch all directors and print them
    cursor.execute("SELECT * FROM directors")
    directors = cursor.fetchall()
    print("Directors:")
    for director in directors:
        print(director)

# Run the tests
if __name__ == "__main__":
    test_movie_operations()
    print("\n")
    test_director_operations()
