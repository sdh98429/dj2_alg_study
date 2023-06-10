import sys
input =sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

ans = 0
for i in range(N):
  for j in range(N):
    ans += abs(X[i]-X[j])
print(ans)