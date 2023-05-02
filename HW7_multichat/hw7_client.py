from socket import *
import threading

port = 2222
BUFFSIZE = 1024

def recvTask(sock):
    while True:
        data = sock.recv(BUFFSIZE) 
        print(data.decode())

sock = socket(AF_INET, SOCK_STREAM) 
sock.connect(('localhost', port))
th = threading.Thread(target=recvTask, args=(sock,)) 
th.start()

my_id = input('ID를 입력하세요: ') 
sock.send(('['+my_id+']').encode())

while True:
    msg_data = input()
    msg = '[' + my_id + '] ' + msg_data
    sock.send(msg.encode())
    if msg_data == 'quit':
        break
    
sock.close()