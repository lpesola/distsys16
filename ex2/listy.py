# lpesola 013470892
import threading
import socket

def writemsg(cs, addr):
    while True:
        msg = cs.recv(1024)
        if not msg:
            break
        print(str(msg.decode("utf-8")))

# read stream until we have the entire message
# write message to cmsg
# if message was G, quit: maybe use a condition for this?

pn = open("port_number")
portno = pn.readline()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), portno))

# listen for incoming connections, max should be 3 (2 x F and 1 x G)
while True:
    s.listen(3)
    (cs, addr) = s.accept()
    ct = threading.Thread(target=writemsg, args=(cs, addr))
    ct.start()
