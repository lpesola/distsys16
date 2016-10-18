# lpesola 013470892

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# listen to port xxx for connections
# assumption: no other programs will connect this socket than the one cat program doing the attack

# wait for message "meow"
# send back "ouch"
