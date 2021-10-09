import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

pair = [[] for _ in range(N+1)] # 자식, 부모 알 수 없기에 이중 리스트에 둘 다 담아두기
for _ in range(N-1):
    a, b = map(int, input().split())
    pair[a] += [b]
    pair[b] += [a]


visited = [0, 1] + [0] * (N-1) # 자식의 부모 노드를 담아두는 역할을 할 것
parent = deque()
parent.append(1) # 루트 노드
while parent: # 부모가 남아있을 때
    p = parent.popleft()
    for child in pair[p]: # 부모 리스트 안에 있는 child
        if not visited[child]: # visited가 아직 없으면 부모 노드로 쓰인 적 없음
            visited[child] = p # 부모 노드 지정
            parent.append(child) # 자식을 새로운 부모로

for i in range(2, N+1):
    print(visited[i])