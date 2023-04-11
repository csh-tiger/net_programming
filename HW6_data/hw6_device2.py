#server2

from socket import *
from random import *

s=socket(AF_INET, SOCK_STREAM)
s.bind(('', 8889))
s.listen(5)

while True:
    c,addr=s.accept()
    
    data=c.recv(1024)
    msg=data.decode()
    if msg=='Request':
        heart=randint(40,140)
        step=randint(2000,6000)
        cal=randint(1000,4000)
        c.send(b'Heartbeat:'+str(heart).encode()+b' Steps:'+str(step).encode()+b' Cal:'+str(cal).encode())
    else:
        break
         
c.close()