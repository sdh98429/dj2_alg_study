import sys
input = sys.stdin.readline

N = int(input())
time = [[0]*2 for _ in range(N)]
for i in range(N):
  time[i] = list(map(int, input().split()))
time.sort(key = lambda x : (x[1], x[0]))

tot = 0
end = 0
for t in time:
  if end <= t[0]:
    tot += 1
    end = t[1]
print(tot)