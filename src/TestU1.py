from addTrainingSes import*
from showmenufucntion import*
from showTrainingHistory import*

def main():
    sessions = []
    in_use = True


    while in_use:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_session(sessions)
        elif choice == "2":
            view_sessions(sessions)
        elif choice == "3":
            print("View summary (not implemented yet)")
        elif choice == "4":
            print("Exiting program. Goodbye!")
            in_use = False
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
