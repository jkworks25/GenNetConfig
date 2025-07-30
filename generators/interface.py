def configure_interface():
    """Gets interface details from the user and generates the configuration."""
    print("\n--- Interface Configuration ---")
    int_type = input("Enter interface type (e.g., GigabitEthernet, FastEthernet): ")
    int_num = input("Enter interface number (e.g., 0/0/1): ")
    description = input("Enter interface description: ")
    ip_address = input("Enter IP address: ")
    subnet_mask = input("Enter subnet mask: ")

    print("\n--- Generated Configuration ---")
    print(f"interface {int_type}{int_num}")
    if description:
        print(f" description {description}")
    if ip_address and subnet_mask:
        print(f" ip address {ip_address} {subnet_mask}")
    print(" no shutdown")
    print("exit")
    print("-----------------------------")
