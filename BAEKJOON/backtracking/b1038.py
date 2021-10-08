from collections import deque
N = int(input())

def bfs():
    cnt = -1
    q = deque()
    for i in range(10):
        q.append(i)

    while q:
        s = q.popleft()
        cnt += 1
        if cnt == N:
            print(s)
            break
        for i in range(s%10):
            q.append(s * 10 + i)
    else:
        print(-1)

bfs()