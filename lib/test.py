from movie import Movie
from director import Director

# Drop and recreate tables for movies and director
Movie.drop_table()
Movie.create_table()

Director.drop_table()
Director.create_table()

# Create instances of Movie and Director,content to save
movie1 = Movie(None, "The Home Coming", "This is a movie about the home coming of american man to Africa.", "Comedy", 142, "2024-09-23")
movie1.save()

movie2 = Movie(None, "The creed", "The dynamis ways of living for the people in the incient.", "Thriller", 175, "2022-03-24")
movie2.save()

director1 = Director(None, "Molly Nzembi", "wbs Entertainment")
director1.save()

director2 = Director(None, "Francis Omondi", "wow wow Pictures")
director2.save()

# Update a movie and a director
movie1.title = "The storm "
movie1.update()

director2.production = "Paramount net"
director2.update()

# Delete a movie and a director
# movie2.delete()
# director1.delete()

# Find by title examples (corrected)
found_movie = Movie.find_by_title("The Home Coming")
if found_movie:
    print("Found Movie:", found_movie)
else:
    print("Movie not found")

found_director = Director.find_by_name("Molly Nzembi")
if found_director:
    print("Found Director:", found_director)
else:
    print("Director not found")

# Fetch all movies and directors
print("\nMovies:")
for movie in Movie.get_all_movies():
    print(movie)

print("\nDirectors:")
for director in Director.get_all_directors():
    print(director)
