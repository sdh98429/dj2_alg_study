N = int(input())

div = 2
while N > 1 and div <= N:
  while not N%div:
    print(div)
    N //= div
  div += 1