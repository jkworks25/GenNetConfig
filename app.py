from generators.interface import configure_interface
from generators.bgp import configure_bgp
from generators.mpls import configure_mpls


def show_main_menu():
    """Displays the main menu."""
    print("\nCisco IOS XE Interactive Config Generator")
    print("=========================================")
    print("1. Configure an Interface")
    print("2. Configure BGP")
    print("3. Configure MPLS")
    print("4. Exit")
    print("=========================================")


def main():
    """Main function to run the application."""
    while True:
        show_main_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            configure_interface()
        elif choice == '2':
            configure_bgp()
        elif choice == '3':
            configure_mpls()
        elif choice == '4':
            print("Exiting application. Goodbye!")
            break
        else:
            print("\n[ERROR] Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
