from generators.interface import configure_interface
from generators.bgp import configure_bgp
from generators.mpls import configure_mpls
from generators.vlan import configure_vlan
from generators.switchport import configure_switchport


def show_main_menu():
    """Displays the main menu."""
    print("\nCisco IOS XE Interactive Config Generator")
    print("=========================================")
    print("1. Configure an Interface")
    print("2. Configure BGP")
    print("3. Configure MPLS")
    print("4. Configure Switching")
    print("5. Exit")
    print("=========================================")

def show_switching_menu():
    """Displays the switching configuration menu."""
    print("\n--- Switching Configuration ---")
    print("1. Configure VLAN")
    print("2. Configure Switchport")
    print("3. Back to main menu")
    print("-----------------------------")
    return input("Enter your choice (1-3): ")

def main():
    """Main function to run the application."""
    while True:
        show_main_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            configure_interface()
        elif choice == '2':
            configure_bgp()
        elif choice == '3':
            configure_mpls()
        elif choice == '4':
            while True:
                switching_choice = show_switching_menu()
                if switching_choice == '1':
                    configure_vlan()
                elif switching_choice == '2':
                    configure_switchport()
                elif switching_choice == '3':
                    break
                else:
                    print("\n[ERROR] Invalid choice. Please enter a number from 1 to 3.")
        elif choice == '5':
            print("Exiting application. Goodbye!")
            break
        else:
            print("\n[ERROR] Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
