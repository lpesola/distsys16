import subprocess
import time
import argparse
import sys


# connect to node bla do action foo

def attack():
    # connect to port, sleep 6 seconds (or should this happen after message is sent?)
    # send meow
    # wait for reply ouch 8 seconds
    # send message G

def search():
    # list processes
    # check if mouse.py
    # sleep 12 s
    # if yes, send message F
    # else exit code 2

    r = subprocess.run("ps -u lpesola | grep mouse.py", shell=True)
    time.sleep(12)
    # 0 = success, 1 = not found
    if r.returncode == "0":
        print("yay")
        # connect to listy, write message F
    sys.exit(r.returncode)


# main begins

parser = argparse.ArgumentParser
parser.add_argument("cmd")
parser.add_argument("cat")
args = parser.parse_args()

if args.cmd == "S":
    search()
elif args.cmd = "A":
    attack()
else:
    sys.exit("no argument given or unknown argument "+args.cmd)