N = int(input())
S1= []
S2= []
for i in range(N):
  if i%2:
    S1.append(' ')
    S2.append('*')
  else:
    S1.append('*')
    S2.append(' ')

for _ in range(N):
  print(*S1, sep="")
  print(*S2, sep="")

  