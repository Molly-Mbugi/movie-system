from director import Director  
from movie import Movie 

def exit_program():
    print("see you later!")
    exit()

#implementation 

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