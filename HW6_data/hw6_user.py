#client

import time
from socket import *


def txt(arg):
    if 'Temp'and 'Humid' and 'Illum' in arg:
        device='Device1'
    elif ' Heartbeat'and 'Steps' and 'Cal' in arg:
        device='Device2'
    data=arg.split(' ')
    list_data1=[]
    list_data2=[]
    for i in data:
        d=i.split(':')
        list_data1.append(d[0])
        list_data2.append(d[1])
        
    text=time.ctime(time.time())+': '+device+': '+list_data1[0]+'='+list_data2[0]+', '+list_data1[1]+'='+list_data2[1]+', '+list_data1[2]+'='+list_data2[2]
    return text

    
while True:  
    num=input('Select device:')
    if num=='quit':
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost',8888))
        s.send(num.encode())
        
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost',8889))
        s.send(num.encode())
        break
    elif int(num)==1:
        s= socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost', 8888))
        s.send(b'Request')
        msg=s.recv(1024).decode()
        txt_save=txt(msg)
        f=open('data.txt', 'a')
        f.write(txt_save+'\n')
        f.close()
    elif int(num)==2:
        s= socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost', 8889))
        s.send(b'Request')
        msg=s.recv(1024).decode()
        txt_save=txt(msg)
        f=open('data.txt', 'a')
        f.write(txt_save+'\n')
        f.close()
    else:
        print('Select device again(1 or 2)')
s.close()