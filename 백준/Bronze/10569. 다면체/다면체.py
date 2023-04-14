import sys
input = sys.stdin.readline
T = int(input())

for tc in range(T):
  V, E = map(int, input().split())
  print(2-V+E)