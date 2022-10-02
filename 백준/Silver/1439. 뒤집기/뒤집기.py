S = input()
cha = 0
if len(S) == 1:
  print(0)
else:
  for i in range(1, len(S)):
    if S[i] != S[i-1]:
      cha += 1
  print(cha//2 + 1 if cha%2 else cha//2)
