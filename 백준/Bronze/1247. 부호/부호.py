import sys
input = sys.stdin.readline

T = 3

for _ in range(T):
  N = int(input())
  tot = 0
  for _ in range(N):
    tot += int(input())
  if not tot:
    print(0)
  else:
    print('+' if tot > 0 else '-')