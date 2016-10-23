# lpesola 013470892
import subprocess
import time
import argparse
import sys
import socket

portno = 0


def sendmsg(msg):
    f = open("listy_location")
    listy = f.readline().rstrip()
    ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    global portno
    ls.connect((listy, portno))
    ls.send(bytes(msg, "utf-8"))


def attack(name):
    # connect to mouse & send meow
    # wait for ouch 8 seconds (the 6 seconds the attack should take, takes place in mouse.py
    # (this is how I understood the instructions which were somewhat vague about this)
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
            msg = "G " + socket.gethostname() + " " + name
            sendmsg(msg)

    except Exception as e:
        print(str(e))


def search(name):
    # check if mouse.py is runinng under current user
    # # if yes, the processes will be printed, I didn't think suppressing the prints was necessary
    uname = subprocess.check_output("whoami").decode("utf-8").rstrip()
    r = subprocess.call([" ps -u " + uname + " -f | grep '[m]ouse.py'"], shell=True)
    # " Jazzy and Catty need 12 seconds to search one node."
    time.sleep(12)
    # 0 = success, 1 = not found
    if r == 0:
        msg = "F " + socket.gethostname() + " " + name
        sendmsg(msg)
    sys.exit(r)


f = open("port_number")
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
    sys.exit("no argument given or unknown argument " + args.cmd)
