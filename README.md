# Cisco IOS XE Interactive Config Generator

## Summary

This is a command-line application designed to help network engineers create Cisco IOS XE configurations quickly and accurately. The tool provides an interactive menu to guide the user through the process of generating configurations for various network features.

## Features

The application currently supports the generation of configurations for:

*   **Interfaces:** Configure basic interface settings, including description, IP address, and subnet mask.
*   **BGP (Border Gateway Protocol):** Set up a basic BGP configuration with a neighbor and advertise a network.
*   **MPLS (Multiprotocol Label Switching):** Enable MPLS globally and on a specific interface.
*   **Switching:**
    *   **VLAN Creation:** Create and name new VLANs.
    *   **Switchport Configuration:** Configure an interface as an access or trunk port.

## Usage

To run the application, you need to have Python 3 installed.

1.  Clone the repository to your local machine.
2.  Navigate to the project directory in your terminal.
3.  Run the application with the following command:

    ```bash
    python3 app.py
    ```

4.  Follow the on-screen prompts to select a feature and provide the necessary configuration details.

## Use Case

This tool is designed for network engineers and students who work with Cisco IOS XE devices. It simplifies the process of creating common configurations, reducing the chance of syntax errors and saving time. By providing a simple interactive menu, it lowers the barrier to entry for generating complex configurations and serves as a helpful tool for day-to-day network operations.
