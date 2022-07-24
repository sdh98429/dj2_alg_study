S = input()

D = dict()
for i in range(26):
  if i <= 17:
    D[chr(i+65)] = i//3 + 2
  if i >= 19:
    D[chr(i+65)] = (i-1)//3 + 2
D['S'] = 7
D['Z'] = 9

ans = 0
for i in range(len(S)):
  ans += D[S[i]]+1
print(ans)