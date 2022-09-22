S = input()
for i in range(len(S)):
  if S[i] != S[-1-i]:
    print(0)
    break
else:
  print(1)