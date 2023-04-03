import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr=s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())
    
    
    #->이름 수신 후 출력
    msg=client.recv(1024)
    print(msg.decode())
    
    #<-본인의 학번 전송(학번, 정수형으로(문자X))
    num=20181533
    client.send(num.to_bytes(4, 'big'))
    
    client.close()