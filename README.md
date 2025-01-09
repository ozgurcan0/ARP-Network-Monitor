# ARP Network Monitor

This Python script monitors the ARP table of a specified IP block and detects any changes in MAC addresses or new devices on the network.

## Requirements

- Python 3.x
- Scapy library

You can install Scapy using pip:
pip install scapy


## Usage

Run the script with the desired IP block as an argument:
python main.py <IP_BLOCK>


For example:
python main.py 192.168.1.0/24

## Functionality

- The script continuously checks the ARP table for the specified IP block.
- It detects changes in MAC addresses and alerts the user.
- It identifies new devices that appear on the network.

## License

This project is licensed under the MIT License.
