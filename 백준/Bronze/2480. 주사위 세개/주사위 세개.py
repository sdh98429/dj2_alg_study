L = list(map(int, input().split()))
L.sort()
if L[2] == L[0]:
  print(L[2]*1000+10000)
elif L[2] == L[1] or L[0]==L[1]:
  print(L[1]*100 + 1000)
else:
  print(L[2]*100)