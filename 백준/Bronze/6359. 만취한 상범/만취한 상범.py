T = int(input())

R = [0] + [1] * 100

for i in range(2, 101):
  j = 1
  while i*j in range(len(R)):
    R[i*j] = 1 - R[i*j]
    j += 1

for tc in range(T):
  n = int(input())
  print(sum(R[1:n+1]))

