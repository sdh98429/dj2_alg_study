T = int(input())

for tc in range(T):
  N = int(input())
  A = N//25
  B = (N-25*A)//10
  C = (N-25*A-10*B)//5
  D = (N-25*A-10*B-5*C)
  print(A, B, C, D)