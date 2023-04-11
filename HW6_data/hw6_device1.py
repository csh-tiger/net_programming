#server1

from socket import *
from random import *

s=socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen(5)

while True:
    c,addr=s.accept()
    
    data=c.recv(1024)
    msg=data.decode()
    if msg=='Request':
        temp=randint(0,40)
        humid=randint(0,100)
        illum=randint(70,150)
        c.send(b'Temp:'+str(temp).encode()+b' Humid:'+str(humid).encode()+b' Illum:'+str(illum).encode())
    else:
        break
         
c.close()