import sys
input = sys.stdin.readline

N, M = map(int, input().split())
D = dict()
for _ in range(N):
  key, value = input().split()
  D[key] = value

for _ in range(M):
  site = input().rstrip()
  print(D[site])