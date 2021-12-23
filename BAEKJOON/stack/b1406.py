# stack !! 에디터
# 개행문자 처리로 많이 틀림, sys.stdin.readline().strip()
# https://hwisaek.tistory.com/entry/Python-sysstdinreadline-%EA%B0%9C%ED%96%89-%EB%AC%B8%EC%9E%90-%EC%B2%98%EB%A6%AC
# 커서 앞의 스택, 커서 뒤의 스택 만들어서 해결

import sys
from collections import deque

W = list(input())

F = deque() # 커서 앞
B = deque() # 커서 뒤

for w in W:
    F.append(w)

N = int(input())

for _ in range(N):
    edit = list(sys.stdin.readline().strip().split()) # 개행문자 \n 도 섞여들어가므로 strip 필수
    if edit[0] == 'L':
        if F: # 커서 앞에 문자열 존재
            e = F.pop()
            B.append(e)
    elif edit[0] == 'D':
        if B: # 커서 뒤에 문자열 존재
            e = B.pop()
            F.append(e)
    elif edit[0] == 'B': # 지우기
        if F:
            e = F.pop()
    else: # 추가하기
        F.append(edit[1])


while F: # 커서 앞은 queue처럼 빼기
    print(F.popleft(), end="")
while B: # 커서 뒤는 stack처럼 빼기
    print(B.pop(), end="")
