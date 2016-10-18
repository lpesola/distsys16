# lpesola 013470892

import socket
import threading
import time
import sys

alive = True
lock = threading.Lock


# wait for message "meow"
# send back "ouch"
def die(s, addr):
	f = s.makefile()
	msg = f.readline()
	if msg == "meow":
		# attack on the mouse "should take 6 seconds" so we wait (though since "the cat will wait 8 seconds for the ouch message"
		# it is a bit unclear whether this 6 seconds is already included in the cat's 8 second wait)
		time.sleep(6)
		f.write("ouch")
		f.flush()
		global alive
		global lock
		lock.acquire()
		alive = False
		lock.release()

# listen to the port defined in port_number for connections
# assumption: only the one cat program doing the attack will connect so after we get the
# first connection we can die


f = open("port_number", "r")
portno = f.readline()
f.close()

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((socket.gethostname(), portno))
except:
	print ("can't bind to port")

while alive:
	s.listen()
	(cs, addr) = s.accept()
	mouset = threading.Thread(target=die, args=(cs, addr))
	mouset.start()
	mouset.join()
	s.close()





