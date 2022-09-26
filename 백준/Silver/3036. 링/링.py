def GCD(a, b):
  while b>0:
    b, a = a%b, b
  return a

N = int(input())

R = list(map(int, input().split()))

for r in R[1:]:
  DIV = GCD(R[0], r)
  print(R[0]//DIV, '/', r//DIV, sep="")