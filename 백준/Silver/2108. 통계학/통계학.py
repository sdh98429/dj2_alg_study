import sys
input = sys.stdin.readline

N = int(input())

L = []
for _ in range(N):
  L.append(int(input()))
L.sort()
print(round(sum(L)/N))
print(L[(N-1)//2])

cnt = 1
max_cnt = 0
before= L[0]
many = [before]


for i in range(1, N):
  if L[i] == before:
    cnt += 1
  if L[i] != before or i == N-1:
    if max_cnt < cnt:
      max_cnt = cnt
      many = [before]
    elif max_cnt == cnt:
      many.append(before)
    before = L[i]
    cnt = 1

print(many[0] if len(many) == 1 else many[1])
print(L[-1]-L[0])