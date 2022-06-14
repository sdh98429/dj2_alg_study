N, M = map(int, input().split())
L = list(map(int, input().split()))

ans = 0

def comb(idx, cnt, tot):
  global L, ans

  if cnt == 3:
    if tot <= M:
      if M - tot <= M - ans:
        ans = tot
    return

  if idx == N:
    return
    
  comb(idx+1, cnt, tot)
  comb(idx+1, cnt+1, tot+L[idx])

comb(0, 0, 0)

print(ans)