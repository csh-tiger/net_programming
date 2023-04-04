from socket import *

s=socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg=input('Enter an expression to calculate:')  #계산식 입력
    if msg=='q':
        break
    s.send(msg.encode())    #계산식 전송
    
    print('Calculation result:', s.recv(1024).decode()) #결과 출력
s.close()