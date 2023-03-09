N = int(input())
L = []
for _ in range(N):
  L.append(input())
L.sort()
first = L[0][0]
Ans = []
num = 1
for i in range(1, len(L)):
  if L[i][0] == L[i-1][0]:
    num += 1
    if num == 5:
      Ans.append(L[i][0])
  else:
    num = 1
if not Ans:
  print('PREDAJA')
else:
  print(''.join(Ans))