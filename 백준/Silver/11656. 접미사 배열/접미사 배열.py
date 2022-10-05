S = input()

L = []

for i in range(len(S)):
  L.append(S[i:])
L.sort()
print(*L, sep="\n")