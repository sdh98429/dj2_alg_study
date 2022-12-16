def GCD(a, b):
  while b:
    b, a = a%b, b
  return a

A_1, B_1 = map(int, input().split())
A_2, B_2 = map(int, input().split())

gcd = GCD(A_1*B_2+A_2*B_1,B_1*B_2)
print((A_1*B_2+A_2*B_1)//gcd,B_1*B_2//gcd)