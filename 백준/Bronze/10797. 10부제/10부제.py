N = int(input())
L = list(map(int ,input().split()))

ans = 0
for l in L:
  if l%10 == N:
    ans += 1
print(ans)