flag = False

H = []
for _ in range(9):
  H.append(int(input()))

def recursion(n, L, tot):
  global flag
  if len(L) == 7 and tot == 100:
    L.sort()
    print(*L, sep="\n")
    flag = True
    return
  if flag:
    return
  if n == 9 or len(L) > 7:
    return
  recursion(n+1, L+[H[n]], tot+H[n])
  recursion(n+1, L, tot)

recursion(0, [], 0)