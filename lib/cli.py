from director import Director  
from movie import Movie 

def print_menu():
    """Prints the main menu options."""
    print("\nPlease select an option:")
    print("1. Manage Directors")
    print("2. Manage Movies")
    print("0. Exit")

    
def list_directors():
    """Lists all directors."""
    directors = Director.get_all_directors()
    for director in directors:
            print(director)

