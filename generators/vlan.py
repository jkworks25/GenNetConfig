def configure_vlan():
    """Gets VLAN details from the user and generates the configuration."""
    print("\n--- VLAN Configuration ---")
    vlan_id = input("Enter VLAN ID (1-4094): ")
    vlan_name = input("Enter VLAN name (optional): ")

    print("\n--- Generated Configuration ---")
    print(f"vlan {vlan_id}")
    if vlan_name:
        print(f" name {vlan_name}")
    print("exit")
    print("-----------------------------")
