# lpesola 013470892

import socket
import threading
import time
import sys

alive = True
lock = threading.Lock()


# wait for message "meow"
# send back "ouch"
def die(s, addr):
    # attack on the mouse "should take 6 seconds" so we wait (though since "the cat will wait 8 seconds for the ouch message"
    # it is a bit unclear whether this 6 seconds is already included in the cat's 8 second wait)
    print("in thread, sleep")
    time.sleep(6)
    print("woke up")
    f = s.makefile("rw")
    print("now has a file")
    msg = f.readline()
    print("read a line")
    if msg == "MEOW":
        f.write("ouch")
        f.flush()
        print("wrote ouch")
        global alive
        global lock
        lock.acquire()
        print("got lock, not live anymore")
        alive = False
        lock.release()

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

i = 0
while alive:
    # there should be only one connection incoming for the cat
    s.listen(2)
    (cs, addr) = s.accept()
    print("round "+str(i))
    i += 1
    mouset = threading.Thread(target=die, args=(cs, addr))
    mouset.start()
    mouset.join()
    s.close()




