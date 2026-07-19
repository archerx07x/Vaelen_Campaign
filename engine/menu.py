from engine.new_game import start_new_game

def show_main_menu():
    print("=================================")
    print("           VAELEN")
    print("=================================")
    print("1. New Game")
    print("2. Load Game")
    print("3. Settings")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        start_new_game()
    elif choice == "2":
        print("Loading a game...")
    elif choice == "3":
        print("Opening settings...")
    elif choice == "4":
        print("Goodbye!")
    else:
        print("Invalid choice.")