import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
  cmd = int(input())
  if cmd:
    heapq.heappush(heap, cmd)
  else:
    if len(heap):
      print(heapq.heappop(heap))
    else:
      print(0)