N = int(input())
while N != 1:
  if N%2:
    print(0)
    break
  N //= 2
else:
  print(1)