N = input()

L = [0] * 10
for s in N:
  if s == '6':
    L[9] += 1
  else:
    L[int(s)] += 1
ans = max(max(L[0:9]), L[9]//2 if not L[9]%2 else L[9]//2+1)
print(ans)