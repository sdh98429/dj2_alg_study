# stack ! 과제는 끝나지 않아!
# 효율 고려 X, 하나 넣고 하나 빼기

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

S = deque() # 과제 넣어두는 스택
tot = 0 # 총 점수
for _ in range(N):
    W = list(map(int, input().split()))
    if W[0]: # 새 과제가 있다면
        if W[2] == 1: # 지금 바로 끝낼 수 있으면 점수 바로 더해주기
            tot += W[1]
        else: # 아니라면 시간 1 빼서 S에 넣어주기
            S.append([W[1], W[2]-1])
    else: # 새 과제가 없다면
        if S: # 남은 과제 있을 때
            n_score, n_time = S.pop()
            if n_time == 1: # 지금 끝낼 수 있으면 점수 더하고
                tot += n_score
            else: # 못 끝내면 시간만 1 빼주기
                S.append([n_score, n_time-1])

print(tot)