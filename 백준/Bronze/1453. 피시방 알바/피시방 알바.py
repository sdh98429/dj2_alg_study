N = int(input())
L = [False] * 100

C = list(map(int, input().split()))

tot = 0
for c in C:
  if L[c-1]:
    tot += 1
  else:
    L[c-1] = True
print(tot)