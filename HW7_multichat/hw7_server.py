from socket import *
import threading
import time

port=2222
BUFFSIZE=1024

def sendTask(sock,addr):
    while True:
        data=sock.recv(BUFFSIZE)
        if 'quit' in data.decode():
            if sock in clients:
                print(addr, 'exited')
                clients.remove(sock)
                break
        print(time.asctime()+str(addr)+':'+data.decode())
        
        for client in clients:
            if client != sock:
                client.send(data)
    sock.close()

clients=[]     
s=socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(3)
while True:
    conn, addr=s.accept()
    clients.append(conn)
    print('new client', addr)
    th=threading.Thread(target=sendTask, args=(conn,addr))
    th.start()