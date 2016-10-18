import subprocess
import time
import argparse
import sys


# connect to node bla do action foo

def attack(name):
    pass
    # connect to port
    # send meow
    # wait for reply ouch 8 seconds
    # send message G

def search(name):
    # check if mouse.py is runinng under my username and sleep for 12 seconds
    # if yes, send message F to cordy
    # else exit code 2

    r = subprocess.call(["ps", "-a | grep mouse.py"])
    time.sleep(2) # CHANGE THIS TO 12 FOR FINAL VERSION, during testing searching should be faster
    # 0 = success, 1 = not found
    if r.returncode == "0":
        print(name+" found mouse")
        # connect to listy, write message F
    sys.exit(r.returncode)


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