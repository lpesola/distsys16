import subprocess
import time
import argparse
import sys
import socket

portno = 0

def sendmsg(msg):
    f = open("/cs/home/lpesola/distsys16/ex2/listy_location")
    listy = f.readline().rstrip()
    ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    global portno
    ls.connect((listy, portno))
    ls.send(bytes(msg, "utf-8"))
    print("sent " + msg)

def attack(name):
    # connect to mouse & send meow
    # wait for ouch 8 seconds
    # send message G
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        global portno
        s.connect((socket.gethostname(), portno))
        channel = s.makefile("rw")
        channel.write("MEOW")
        channel.flush()
        time.sleep(8)
        msg = channel.readline()
        if msg == "OUCH":
            print("got the mouse, inform listy")
            try:
                f.close()
                s.close()
            except Exception as e:
                print(str(e))
            print("close old connection")
            msg = "G "+socket.gethostname()+" "+name
            sendmsg(msg)

    except Exception as e:
        print(str(e))

def search(name):
    # check if mouse.py is runinng under current user and sleep for 12 seconds
    # if yes, send message F to cordy
    # else exit code 2
    uname = subprocess.check_output("whoami").decode("utf-8").rstrip()
    r = subprocess.call([" ps -u "+uname+" -f | grep '[m]ouse.py'"], shell=True)
    time.sleep(3) # CHANGE THIS TO 12 FOR FINAL VERSION, during testing searching should be faster
    # 0 = success, 1 = not found
    if r == 0:
        msg = "F "+socket.gethostname()+" "+name
        sendmsg(msg)
    sys.exit(r)


# main begins
f = open("/cs/home/lpesola/distsys16/ex2/port_number")
portno = int(f.readline().rstrip())
f.close()

parser = argparse.ArgumentParser()
parser.add_argument("cmd")
parser.add_argument("cat")
args = parser.parse_args()

if args.cmd == "S":
    search(args.cat)
elif args.cmd == "A":
    attack(args.cat)
else:
    sys.exit("no argument given or unknown argument "+args.cmd)
