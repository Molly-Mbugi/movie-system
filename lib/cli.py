from helpers import(
   exit_program, 
   list_directors,
   find_directors_by_name,
   create_directors,
   update_directors,
   delete_directors,
   find_movies_by_name,
   create_movies,
   update_movies,
   delete_movies,
   list_movies

)
def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_directors()
        elif choice == "2":
            find_directors_by_name()
        elif choice == "3":
            create_directors()
        elif choice == "4":
            update_directors()
        elif choice == "5":
            delete_directors()
        elif choice == "6":
            find_movies_by_name()
        elif choice == "7":
            create_movies()
        elif choice == "8":
            update_movies()
        elif choice == "9":
            delete_movies()
        elif choice == "10":
            list_movies()
        
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit")
    print("1. List all Directors")
    print("2. Find Directors by name")
    print("3: Create Directors")
    print("4: Update Directors")
    print("5: Delete Directors")
    print("6. Find Movies by name")
    print("7: Create Movies")
    print("8: Update Movies")
    print("9: Delete Movies")
    print("10: List all Movies")


if __name__ == "__main__":
    main()


