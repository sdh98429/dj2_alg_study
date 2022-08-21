ans = 0
for i in range(8):
  S = input()
  for j in range(len(S)):
    if not i%2:
      if not j%2 and S[j] == 'F':
        ans += 1
    else:
      if j%2 and S[j] == 'F':
        ans += 1
print(ans)