L = []
for _ in range(28):
  L.append(int(input()))

for i in range(1, 31):
  if i not in L:
    print(i)