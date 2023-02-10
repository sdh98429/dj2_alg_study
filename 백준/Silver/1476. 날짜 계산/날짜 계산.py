E, S, M = map(int, input().split())

ans = 1
e, s, m = 1, 1, 1
while True:
  if E == e and S == s and M == m:
    print(ans)
    break
  e = e%15 + 1
  s = s%28 + 1
  m = m%19 + 1
  ans += 1