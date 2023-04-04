from socket import *

s=socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    
    while True:
        data=client.recv(1024)  #계산식 수신
        if not data:  #비어있는 데이터 수신 받으면
            break
        try:
            ex=data.decode()
            if '+' in ex :
                sign='+'
            elif '-' in ex:
                sign='-'
            elif '*' in ex:
                sign='*'
            else:
                sign='/'
            ex=ex.split(sign)
        except: #try가 에러면 except로
            client.send(b'Try again')
        else:   #try가 에러가 아니면 else로 / 계산식 계산
            ex=list(map(int, ex))
            if sign=='+':
                ex=ex[0]+ex[1]
            elif sign=='-':
                ex=ex[0]-ex[1]
            elif sign=='*':
                ex=ex[0]*ex[1]
            else:
                ex=round(float(ex[0]/ex[1]),1)
            ex_re=str(ex)
            client.send(ex_re.encode())   #결과 전송
    client.close()