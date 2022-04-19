# 명령 프롬프트

T = int(input())
names = [] # 파일 이름들
ans = '' # 정답

for tc in range(1, T+1):
    names.append(input()) # 파일 이름들 입력 받기

for i in range(len(names[0])): # 글자수
    now = names[0][i] # 현재 글자
    for name in names[1:]: # 나머지 파일 이름들에서
        if now != name[i]: # 만약 현재 글자가 다르다면 ? 표시하고 break
            ans = ans + '?'
            break
    else: # 다 일치한다면 현재 글자 더하기
        ans = ans + now

print(ans)
