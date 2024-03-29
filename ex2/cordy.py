# lpesola 013470892

import queue
import subprocess
import threading
import sys

# Queue is thread safe so we can use it to store the nodes the cats need to search
# Search order doesn't matter: the important thing is that the cats don't search the same nodes
nodes = queue.Queue()

def search(name):
    while not nodes.empty():
        node =  nodes.get()
        # 0 = found, 1 = not found
        command = "python3 distsys16/ex2/chase_cat.py S "+name
        r = subprocess.call(["ssh", node, command])
        if r == 0:
            return
        elif r == 1:
            continue
        else:
            sys.exit("something unexpected happened")

n = open("ukkonodes", "r")
for line in n:
    nodes.put(line.rstrip())

catty = threading.Thread(target=search, args=("catty",))
catty.daemon = True
jazzy = threading.Thread(target=search, args=("jazzy",))
jazzy.daemon = True
catty.start()
jazzy.start()


# read cmsg, wait until you find a line beginning with an F(ound the mouse) or G(ot the mouse)
# message format: F/G ukkoXXX catname
# 1st F -> make other cat search the same node
# 2n F -> make catty attack
# G -> quit

# assumption: cmsg file exists AND it is empty (this was not specified in the assignment text)
fcount = 0
cmsg = open("cmsg", "r") # read text is default mode for open, we don't need to write anything
while True:
     msg = cmsg.read()
     if msg == '' or msg=="\n":
         continue
     else:
         msg = msg.split(" ")
         node = msg[1]
         cat = msg[2]
         if msg[0] == "F":
             fcount += 1
             if fcount == 1:
                 # make other cat search for the same node
                 if cat == "catty":
                     r = subprocess.call(["ssh", node, "python3 distsys16/ex2/chase_cat.py S jazzy"])
                 elif cat == "jazzy":
                     r = subprocess.call(["ssh", node, "python3 distsys16/ex2/chase_cat.py S catty"])
             if fcount == 2:
                 # whichever cat can attack: we'll just stick to the same cat since this was not specified
                r = subprocess.call(["ssh", node, "python3 distsys16/ex2/chase_cat.py A catty"])
         elif msg[0] == "G":
             # cat got the mouse, stop
             pass
             sys.exit(cat+" caught the mouse in node "+node)


