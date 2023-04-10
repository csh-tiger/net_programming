from socket import *

def send():
    c.send(b'HTTP/1.1 404 Not Found\r\n')
    str='Content-Type: ' + mimeType + '\r\n'
    c.send(str.encode())
    c.send(b'\r\n')

s=socket()
s.bind(('', 80))
s.listen(10)

while True:
    c,addr=s.accept()
    
    data=c.recv(1024)
    msg=data.decode()
    req=msg.split('\r\n')
    
    req=req[0]  #첫번째 줄만 따와(GET)
    
    if 'index.html' in req:
        req=req.split(' ')
        req=req[req.index('/index.html')]
        filename=req[req.find('index'):]
        f = open(filename,'r', encoding='utf-8')
        mimeType = 'text/html'
        send()
        sdata=f.read()
        c.send(sdata.encode('euc-kr'))
    
    elif 'iot.png' in req:
        req=req.split(' ')
        req=req[req.index('/iot.png')]
        filename=req[req.find('iot'):]
        f=open(filename, 'rb')
        mimeType='image/png'
        send()
        sdata=f.read()
        c.send(sdata)
        
    elif 'favicon.ico' in req:
        req=req.split(' ')
        req=req[req.index('/favicon.ico')]
        filename=req[req.find('favicon'):]
        f = open(filename, 'rb')
        mimeType = 'image/x-icon'
        send()
        sdata=f.read()
        c.send(sdata)

        
    else:
        print('404')
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')
        
    c.close()