import sys
input = sys.stdin.readline

N = int(input())
D = dict()

for _ in range(N):
  name, cmd = input().split()
  if cmd == 'enter':
    D[name] = 1
  else:
    del D[name]
print(*sorted(D, reverse=True), sep='\n')