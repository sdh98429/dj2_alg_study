N = int(input())
ans = 0
while N:
  ans += N//5
  N //= 5
print(ans)