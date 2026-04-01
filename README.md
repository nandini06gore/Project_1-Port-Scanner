# Project_1-Port-Scanner
Python Threaded TCP Port Scanner A lightweight, high-performance TCP port scanner built with Python. This project demonstrates the fundamentals of socket programming, multi-threading, and network reconnaissance.  

Features
TCP Connect Scanning: Uses the socket library to perform a full three-way handshake.

Multi-threaded: Leverages Python’s threading module to scan multiple ports concurrently, significantly reducing scan time.

Flexible Input: Supports scanning single hosts (IP or Domain) and customizable port ranges.

Logging & Output: Real-time console output with results automatically logged to a .txt file for later analysis.

Exception Handling: Gracefully handles timeouts, invalid hostnames, and user interrupts.

🛠️ Technical Implementation
The scanner works by attempting to establish a connection using socket.connect_ex().

How it works:

Returns 0: The port is Open (the handshake was successful).

Returns Error Code: The port is Closed or filtered by a firewall.

Prerequisites
Python 3.x

No external libraries required (uses standard library modules: socket, threading, datetime).

Usage
Clone the repository:

Bash
git clone https://github.com/nandini06gore/python-port-scanner.git
Run the script:

Bash
python scanner.py
Enter the target host and the range of ports you wish to scan.

Disclaimer
This tool is for educational and ethical testing purposes only. Never scan a host or network without explicit permission.
