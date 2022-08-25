import math
T = int(input())

for tc in range(T):
  A, B = map(int, input().split())
  print(math.factorial(B)//(math.factorial(B-A)*math.factorial(A)))
  