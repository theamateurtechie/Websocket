import socket

HEADER=64
PORT=7777
SERVER='127.0.1.1'
DISCONNECT_MESSAGE='!Disconnect'
ADDR=(SERVER,PORT)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)