def subnet_mask_from_cidr(cidr):
    """Converts CIDR prefix length to a subnet mask."""
    try:
        prefix = int(cidr)
        if not 0 <= prefix <= 32:
            return None

        mask = (0xffffffff << (32 - prefix)) & 0xffffffff
        return ".".join([str((mask >> i) & 0xff) for i in [24, 16, 8, 0]])
    except (ValueError, TypeError):
        return None

def configure_bgp():
    """Gets BGP details from the user and generates the configuration."""
    print("\n--- BGP Configuration ---")
    asn = input("Enter your BGP AS number: ")
    neighbor_ip = input("Enter neighbor IP address: ")
    remote_as = input("Enter neighbor remote AS number: ")
    network_input = input("Enter network to advertise (e.g., 192.168.2.0/24) (optional): ")

    print("\n--- Generated Configuration ---")
    print(f"router bgp {asn}")
    print(f" neighbor {neighbor_ip} remote-as {remote_as}")

    if network_input:
        network_parts = network_input.split('/')
        if len(network_parts) == 2:
            network_address = network_parts[0]
            cidr_prefix = network_parts[1]
            subnet_mask = subnet_mask_from_cidr(cidr_prefix)
            if subnet_mask:
                print(f" network {network_address} mask {subnet_mask}")
            else:
                print(f" ! Invalid CIDR prefix: /{cidr_prefix}. Could not generate network command.")
        else:
            print(f" ! Invalid network format: '{network_input}'. Please use format like 192.168.2.0/24.")

    print("exit")
    print("-----------------------------")
