S = input()
L = [0] * 26
for s in S:
  L[ord(s)-97] += 1
print(*L)