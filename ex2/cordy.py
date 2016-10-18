import queue # Queue is thread safe, ordering doesn't matter as long as the cats don't search the same nodes
import subprocess
import threading
import time # MUISTA OTTAA POIS KUN TESTI UKOLLA
import sys

nodes = queue.Queue()
def search(name):
    while not nodes.empty():
        node =  nodes.get()
        time.sleep(1) # MUISTA OTTAA POIS LOPULLISESTA
        print (name + node)
        # ssh lpesola@ **node** chase_cat.py S name
        # 0 = found, 1 = not found
        #r = subprocess.run(["ssh", name], shell=True)
    else:
        return

# main starts here
n = open("ukkonodes", "r")
for line in n:
    nodes.put(line)

catty = threading.Thread(target=search, args=("catty",))
jazzy = threading.Thread(target=search, args=("jazzy",))
catty.start()
jazzy.start()

# sit pitäs kans lukee sitä filua siltä varalta että siellä ois found
# F/G ukkoXXX catname
# jos on found niin..

cmsg = open("cmsg") # read text is default mode for open, we don't need to write anything

while True:
    msg = cmsg.read()
    if msg == '':
        continue
    else:
        msg = msg.split(" ")
        node = msg[1]
        cat = msg[2]
        if msg[0] == "F":
            # make other cat search the same node
            break
        elif msg[0] == "G":
            pass
            sys.exit(cat+" caught the mouse in node "+node)
        else:
            print ("thats weird")
            break




# subprocess run ssh chase_cat.py S ei-F-cat
