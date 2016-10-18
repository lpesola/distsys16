import subprocess
import time
import argparse
import sys
import socket


# connect to node bla do action foo

def attack(name):
    # connect to mouse & send meow
    # wait for ouch 8 seconds
    # send message G
    f = open("port_number")
    portno = int(f.readline().rstrip())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), portno))
    channel = s.makefile()
    channel.write("MEOW")
    channel.flush()
    time.sleep(8)
    msg = channel.readline()
    print(msg)

def search(name):
    # check if mouse.py is runinng under my username and sleep for 12 seconds
    # if yes, send message F to cordy
    # else exit code 2
    uname = subprocess.check_output("whoami").decode("utf-8").rstrip()
    r = subprocess.call([" ps -u "+uname+" -f | grep '[m]ouse.py'"], shell=True)
    time.sleep(2) # CHANGE THIS TO 12 FOR FINAL VERSION, during testing searching should be faster
    # 0 = success, 1 = not found
    if r == 0:
        # connect to listy, write message F
        pass
    sys.exit(r)


# main begins

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