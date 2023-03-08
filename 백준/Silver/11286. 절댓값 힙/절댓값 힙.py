import sys, heapq
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
  cmd = int(input())
  if cmd:
    heapq.heappush(heap, (abs(cmd), 1 if cmd >= 0 else -1))
  else:
    if heap:
      amount, sign = heapq.heappop(heap)
      print(amount * sign)
    else:
      print(0)