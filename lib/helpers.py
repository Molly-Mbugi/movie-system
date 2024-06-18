from director import Director  
from movie import Movie 

def exit_program():
    print("See you later!")
    exit()

# Directors implementation 

def list_directors():
    directors = Director.get_all_directors()
    if directors:
        for director in directors:
            print(director)
    else:
        print("No directors found.")

def find_directors_by_name():
    name = input("Enter the director's name: ")
    director = Director.find_by_name(name)
    print(director) if director else print(f"Director {name} not found")  

def create_directors():
    name = input("Enter the director's name: ")
    production = input("Enter the department's production: ")
    try:
        director = Director.create(name, production)
        print(f"Success: {director}")
    except Exception as exc:
        print("Error creating director: ", exc)

def update_directors():
    name = input("Enter the director's name to update: ")
    director = Director.find_by_name(name)
    if director:
        try:
            new_name = input("Enter the director's new name: ")
            director.name = new_name
            new_production = input("Enter the director's new production: ")
            director.production = new_production

            director.update()
            print(f"Success: {director}")
        except Exception as exc:
            print("Error updating director: ", exc)
    else:
        print(f"Director {name} not found")

def delete_directors():
    name = input("Enter the director's name to delete: ")
    director = Director.find_by_name(name)
    if director:
        director.delete()
        print(f"Director {name} deleted")
    else:
        print(f"Director {name} not found")

# Movies implementation

def list_movies():
    movies = Movie.get_all_movies()
    if movies:
        for movie in movies:
            print(movie)
    else:
        print("No movies found.")

def find_movies_by_name():
    name = input("Enter the movie's name: ")
    movie = Movie.find_by_name(name)
    print(movie) if movie else print(f"Movie {name} not found")

def create_movies():
    title = input("Enter the title of the movie: ")
    genre = input("Enter the genre of the movie: ")
    about = input("Enter a description of the movie (optional): ")
    duration = int(input("Enter the duration of the movie in minutes: "))
    release_date = input("Enter the release date of the movie (YYYY-MM-DD): ")

    directors = Director.get_all_directors()
    if directors:
        for idx, director in enumerate(directors, 1):
            print(f"{idx}. {director.name}")
        director_choice = int(input("Choose the director (enter number): "))
        director_id = directors[director_choice - 1].id
    else:
        print("No directors available to assign.")
        director_id = None
    
    try:
        movie = Movie.create(title=title, genre=genre, about=about, duration=duration, release_date=release_date, director_id=director_id)
        print(f"Success: {movie}")
    except Exception as exc:
        print("Error creating movie: ", exc)

def update_movies():
    id_ = input("Enter the movie's ID to update: ")
    movie = Movie.find_by_id(id_)
    if movie:
        try:
            title = input("Enter the movie's new title: ")
            movie.title = title
            genre = input("Enter the movie's new genre: ")
            movie.genre = genre
            about = input("Enter a new description of the movie (optional): ")
            movie.about = about
            duration = int(input("Enter the new duration of the movie in minutes: "))
            movie.duration = duration
            release_date = input("Enter the new release date of the movie (YYYY-MM-DD): ")

            directors = Director.get_all_directors()
            if directors:
                for idx, director in enumerate(directors, 1):
                    print(f"{idx}. {director.name}")
                director_choice = int(input("Choose the new director (enter number): "))
                movie.director_id = directors[director_choice - 1].id
            else:
                print("No directors available to assign.")
                movie.director_id = None

            movie.update()
            print(f"Success: {movie}")
        except Exception as exc:
            print("Error updating movie: ", exc)
    else:
        print(f"Movie ID {id_} not found")

def delete_movies():
    id_ = input("Enter the movie's ID to delete: ")
    movie = Movie.find_by_id(id_)
    if movie:
        movie.delete()
        print(f"Movie ID {id_} deleted")
    else:
        print(f"Movie ID {id_} not found")


     
   

       