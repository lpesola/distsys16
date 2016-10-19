# lpesola 013470892
import threading
import socket

lock = threading.Lock()
cmsg = open("/cs/home/lpesola/distsys16/ex2/cmsg", "a")
mousegotten = False
# assumption: the message fits in 1024 bytes AND will be received at once (should hold in this case)
# write message to cmsg
# if message was G, quit: maybe use a condition for this?
def writemsg(cs, addr):
    msg = cs.recv(1024)
    msg = str(msg.decode("utf-8")).rstrip()
    global lock
    global cmsg
    lock.acquire()
    cmsg.write(msg)
    cmsg.flush()
    lock.release()
    if msg[0] == "G":
        global mousegotten
        mousegotten = True
    return



pn = open("/cs/home/lpesola/distsys16/ex2/port_number")
portno = int(pn.readline().strip())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), portno))

# listen for incoming connections, max should be 3 (2 x F and 1 x G)
# the connections should not be simultaneous since the second cat cannot find the mouse before listy has informed cordy about it: that's why the join
while mousegotten == False:
    s.listen(3)
    (cs, addr) = s.accept()
    ct = threading.Thread(target=writemsg, args=(cs, addr))
    ct.daemon = True
    ct.start()
    ct.join()

