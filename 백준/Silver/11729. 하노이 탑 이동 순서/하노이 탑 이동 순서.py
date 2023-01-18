def Hanoi(n, a, b, c):
  if n == 1:
    print(a, c)
    return
  Hanoi(n-1, a, c, b)
  print(a, c)
  Hanoi(n-1, b, a, c)

N = int(input())
tot = 1
for i in range(N-1):
  tot = tot * 2 + 1
print(tot)
Hanoi(N, 1, 2, 3)
