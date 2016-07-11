import sys
import zmq
from time import gmtime, strftime
import json

def listen():
    print('start')
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.connect("tcp://localhost:5557")
    print('connected')
    while True:        
        data = socket.recv_string()
        print('time: ', strftime("%a, %d %b %Y %H:%M:%S", gmtime()))
        print(data)

listen()