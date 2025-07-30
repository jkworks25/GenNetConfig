from generators.interface import configure_interface


def show_main_menu():
    """Displays the main menu."""
    print("\nCisco IOS XE Interactive Config Generator")
    print("=========================================")
    print("1. Configure an Interface")
    print("2. Exit")
    print("=========================================")


def main():
    """Main function to run the application."""
    while True:
        show_main_menu()
        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            configure_interface()
        elif choice == '2':
            print("Exiting application. Goodbye!")
            break
        else:
            print("\n[ERROR] Invalid choice. Please enter a number from 1 to 2.")

if __name__ == "__main__":
    main()
