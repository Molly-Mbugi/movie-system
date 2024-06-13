from director import Director  
from movie import Movie 

def exit_program():
    print("see you later!")
    exit()

# directors implementation 

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
    print(director) if director else print(f'Director{name} not found')  


def create_directors():
    name = input("Enter the directors's name: ")
    production = input("Enter the department's production ")
    try:
        director = Director.create(name, production)
        print(f'Success: {director}')
    except Exception as exc:
        print("Error creating director: ", exc)

def update_directors():
    id_ = input("Enter the directors id: ")
    if director := Director.find_by_id(id_):
        try:
            name = input("Enter the directors new name: ")
            director.name = name
            production = input("Enter the directors's new production: ")
            director.production = production

            director.update()
            print(f'Success: {director}')
        except Exception as exc:
            print("Error updating director: ", exc)
    else:
        print(f'Director {id_} not found')        
def delete_directors():
    id_ = input("Enter the directors's id: ")
    if director := Director.find_by_id(id_):
        director.delete()
        print(f'Director {id_} deleted')
    else:
        print(f'Director {id_} not found')
 # movies implementation       
def list_movies():

    movies = Movie.get_all_movies()
    if movies:
        for movie in movies:
            print(movie)
    else:
        print("No movies found.")

def find_movies_by_name():
    name = input("Enter the Movies's name: ")
    movie = Movie.find_by_name(name)
    print(movie) if movie else print(f'Movie {name} not found')       

def create_movies():
    title = input("Enter the title of the movie: ")
    genre = input("Enter the genre of the movie: ")
    about = input("Enter a description of the movie (optional): ")
    duration = int(input("Enter the duration of the movie in minutes: "))
    release_date = input("Enter the release date of the movie (YYYY-MM-DD): ")
    director_id = int(input("Enter the ID of the director for the movie: "))
    
    try:
        movie = Movie.create(title=title, genre=genre, about=about, duration=duration, release_date=release_date, director_id=director_id)
        print(f'Success: {movie}')
    except Exception as exc:
        print("Error creating Movies: ", exc)  

def update_movies():
    id_ = input("Enter the movies's id: ")
    if movie := Movie.find_by_id(id_):
        try:
            title = input("Enter the title of the movie: ")
            movie.title = title
            genre = input("Enter the genre of the movie: ")
            movie.genre = genre
            about = input("Enter a description of the movie (optional): ")
            movie.about = about
            duration = int(input("Enter the duration of the movie in minutes: "))
            movie.duration = duration
            release_date = input("Enter the release date of the movie (YYYY-MM-DD): ")
            movie.release_date = release_date
            director_id = int(input("Enter the ID of the director for the movie: "))
            movie.director_id = director_id 
            
            movie.update()
            print(f'Success: {movie}')
        except Exception as exc:
            print("Error updating Movie: ", exc)
    else:
        print(f'Movie {id_} not found')
def delete_movies():
    id_ = input("Enter the Movie's id: ")
    if movie := Movie.find_by_id(id_):
        movie.delete()
        print(f'Movie {id_} deleted')
    else:
        print(f'Movie {id_} not found')   

def list_movies():
    movies = Movie.get_all_movies()
    if movies:
        for movie in movies:
            print(movie)
    else:
        print("No movies found.")            
     
   

       