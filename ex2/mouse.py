# lpesola 013470892

import socket
import threading
import time
import sys

alive = True


# wait for message "meow"
# send back "ouch"
def die(s, addr):
    # attack on the mouse "should take 6 seconds" so we wait (though since "the cat will wait 8 seconds for the ouch message"
    # it is a bit unclear whether this 6 seconds is already included in the cat's 8 second wait)
    msg = s.recv(1024)
    msg = str(msg.decode("utf-8"))
    if msg == "MEOW":
        time.sleep(6)
        s.send(b'OUCH')
        global alive
        alive = False

# listen to the port defined in port_number for connections
# assumption: only the one cat program doing the attack will connect so after we get the
# first connection we can die


f = open("port_number", "r")
portno = int(f.readline().rstrip())
f.close()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), portno))
except Exception as e:
    print (str(e))

while alive:
    # assumption: only one program ever connects to us as per the instructions only one cat will attack
    s.listen(2)
    (cs, addr) = s.accept()
    die(cs, addr)

s.close()



