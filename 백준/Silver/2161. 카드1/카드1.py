from collections import deque

N = int(input())
Q = deque()

for i in range(1,N+1):
  Q.append(i)

while Q:
  a = Q.popleft()
  print(a, end=" ")
  if Q:
    
    b = Q.popleft()
    Q.append(b)
  