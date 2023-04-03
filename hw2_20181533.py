#20181533 최성현
str='My name is Choi SoungHyun'
new_str=str.replace(" ", "")

print("문자수:", len(new_str))
print("10번 반복 출력:", str *10)
print("첫 번째 문자:", str[0])
print("처음 4개 문자:", new_str[0:4])
print("마지막 4개 문자:", new_str[-4:])
print("거꾸로 출력:", str[::-1])
print("첫번째, 마지막 문자 제거:", str[1:-1])
print("모두 대문자로:", str.upper())
print("모두 소문자:", str.lower())
print("a를 e로 대체:", str.replace('a', 'e'))