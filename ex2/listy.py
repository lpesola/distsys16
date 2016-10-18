# lpesola 013470892
import threading
import socket

def writemsg(cs, addr):


# listen for messages, write them to file cmsg
# quit when you've written a message beginnig with a 'G'

pn = open("port_number")
portno = pn.readline()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), portno))

while True:
    s.listen()
    (cs, addr) = s.accept()
