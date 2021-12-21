# 포기

from collections import deque

N = int(input())
ans = [(-1, 'X')] * N


Qs = []
for i in range(4):
    q = deque()
    Qs.append(deque())

for i in range(N):
    car = input().split()
    if car[1] == 'A':
        Qs[0].append((int(car[0]),i))
    elif car[1] == 'B':
        Qs[1].append((int(car[0]),i))
    elif car[1] == 'C':
        Qs[2].append((int(car[0]),i))
    elif car[1] == 'D':
        Qs[3].append((int(car[0]),i))
print(Qs)
MAX = 98765432100

now = [[] for _ in range(4)]

# while Qs and now[0] and now[1] and now[2] and now[3]:
for i in range(4):
    if Qs[i] and not now[i]:
        now[i] = Qs[i].popleft()

small = min(now[0][0] if now[0] else MAX, now[1][0] if now[1] else MAX, now[2][0] if now[2] else MAX, now[3][0] if now[3] else MAX)
print(small)
print(now)
for i in range(4):
    if now[i] and now[i][0] == small:
        if not now[(i-1)%4] and ans or now[(i-1)%4][0] != small:
            ans[now[i][1]] = now[i][0]
            now[i] = []
            if Qs[i]:
                now[i] = Qs[i].popleft()
        else:
            now[i] = (now[i][0]+1, now[i][1])

print(ans)


