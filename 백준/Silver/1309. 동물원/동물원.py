N = int(input())

a1, a2, a0 = 1, 1, 1
b1, b2, b0 = 1, 1, 1

for i in range(1, N):
  b0 = a0 + a1 + a2
  b1 = a0 + a2
  b2 = a0 + a1
  a1, a2, a0 = b1, b2, b0
print((b0 + b1 + b2)%9901)