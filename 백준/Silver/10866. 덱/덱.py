import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
deq = deque()

for _ in range(N):
  cmd = list(input().split())
  if cmd[0] == 'push_front':
    deq.appendleft(cmd[1])
  elif cmd[0] == 'push_back':
    deq.append(cmd[1])
  elif cmd[0] == 'pop_front':
    if len(deq):
      print(deq.popleft())
    else:
      print(-1)
  elif cmd[0] == 'pop_back':
    if len(deq):
      print(deq.pop())
    else:
      print(-1)
  elif cmd[0] == 'size':
    print(len(deq))
  elif cmd[0] == 'empty':
    print(0 if len(deq) else 1)
  elif cmd[0] == 'front':
    if len(deq):
      left = deq.popleft()
      print(left)
      deq.appendleft(left)
    else:
      print(-1)
  elif cmd[0] == 'back':
    if len(deq):
      right = deq.pop()
      print(right)
      deq.append(right)
    else:
      print(-1)
  
  
      
    