import sys
N = int(sys.stdin.readline().rstrip())
tot = 1
for _ in range(N):
  tot += int(sys.stdin.readline().rstrip())-1
print(tot)