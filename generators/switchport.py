def configure_switchport():
    """Gets switchport details from the user and generates the configuration."""
    print("\n--- Switchport Configuration ---")
    interface_name = input("Enter the interface to configure (e.g., GigabitEthernet0/0/1): ")
    mode = input("Enter switchport mode (access/trunk): ").lower()

    print("\n--- Generated Configuration ---")
    print(f"interface {interface_name}")

    if mode == 'access':
        access_vlan = input("Enter access VLAN ID: ")
        print(" switchport mode access")
        print(f" switchport access vlan {access_vlan}")
    elif mode == 'trunk':
        native_vlan = input("Enter native VLAN ID (optional): ")
        allowed_vlans = input("Enter allowed VLANs (e.g., 10,20,30 or 'all') (optional): ")
        print(" switchport mode trunk")
        if native_vlan:
            print(f" switchport trunk native vlan {native_vlan}")
        if allowed_vlans:
            if allowed_vlans.lower() == 'all':
                print(" switchport trunk allowed vlan all")
            else:
                print(f" switchport trunk allowed vlan {allowed_vlans}")
    else:
        print(f"! Invalid mode: {mode}. Please choose 'access' or 'trunk'.")

    print("exit")
    print("-----------------------------")
