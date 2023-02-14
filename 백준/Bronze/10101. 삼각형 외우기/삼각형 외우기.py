L = [int(input()) for _ in range(3)]
L.sort()
if (L[0] == L[1]) and (L[1] == L[2]) and sum(L)==180:
  print('Equilateral')
elif ((L[0]==L[1]) or (L[1]==L[2])) and sum(L)==180:
  print('Isosceles')
elif sum(L) == 180:
  print('Scalene')
else:
  print('Error')