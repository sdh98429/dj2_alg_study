import sys
input = sys.stdin.readline # 이 코드 안 쓰면 시간 초과 납니다

N, W = map(int, input().split()) # 노드의 수 N, 고인 물의 양 W

flag = [0, 0] + [1] * (N-1)
leaf = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split()) #list 사용하면 시간 초과 잘 떠서 map으로 간선의 정보 받기
    for i in [a,b]:
        if flag[i]:
            leaf[i] = 1
            flag[i] = 0
        else:
            leaf[i] = 0

print(W/sum(leaf))
