tot = 0
N = int(input())
for _ in range(N):
  a, b = map(int, input().split())
  tot += b%a
print(tot)