e, f, c = map(int, input().split())
empty = e + f
ans = 0
while empty >= c:
  new = empty//c
  ans += new
  empty = empty - new * c + new
print(ans)