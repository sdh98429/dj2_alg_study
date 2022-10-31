M = int(input())
N = int(input())
Square = []
for i in range(1, int(10000**0.5)+1):
  if M <= i**2 and N >= i**2:
    Square += [i**2]
if Square:
  print(sum(Square))
  print(Square[0])
else:
  print(-1)