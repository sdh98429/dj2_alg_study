T = int(input())

for tc in range(T):
  two = bin(int(input()))[::-1]
  L = []
  for i in range(len(two)-2):
    if two[i] == '1':
      L.append(i)
  print(*L)