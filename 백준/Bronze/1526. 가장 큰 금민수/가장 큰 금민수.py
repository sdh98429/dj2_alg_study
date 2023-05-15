N = int(input())

for i in range(N, 0, -1):
  for s in list(str(i)):
    if not (s in ['4', '7']):
      break
  else:
    print(i)
    break
      