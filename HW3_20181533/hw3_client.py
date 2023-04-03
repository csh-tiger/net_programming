import socket

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr=('localhost', 9000)



sock.connect(addr)

msg1=sock.recv(1024)
print(msg1.decode())

#본인 이름 문자열로 전송->
sock.send(b'Sounghyun Choi')


#학번 수신 후 출력<-

msg2=sock.recv(1024)
print(int.from_bytes(msg2,'big'))

sock.close()