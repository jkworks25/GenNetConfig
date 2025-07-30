def configure_mpls():
    """Generates a basic MPLS configuration."""
    print("\n--- MPLS Configuration ---")
    interface_name = input("Enter the interface to enable MPLS on (e.g., GigabitEthernet0/0/1): ")

    print("\n--- Generated Configuration ---")
    print("! Enable Cisco Express Forwarding (CEF)")
    print("ip cef")
    print("\n! Enable MPLS globally")
    print("mpls ip")

    if interface_name:
        print(f"\n! Enable MPLS on the interface")
        print(f"interface {interface_name}")
        print(" mpls ip")
        print("exit")

    print("-----------------------------")
