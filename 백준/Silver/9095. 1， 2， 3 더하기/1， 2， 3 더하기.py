T = int(input())

n1 = [1] + [0] * 10
n2 = [0, 1] + [0] * 9
n3 = [0, 0, 1] + [0] * 8
for i in range(11):
  if i>= 1:
    n1[i] = n1[i-1] + n2[i-1] + n3[i-1]
  if i >= 2:
    n2[i] = n1[i-2] + n2[i-2] + n3[i-2]
  if  i>= 3:
    n3[i] = n1[i-3] + n2[i-3] + n3[i-3]

for tc in range(T):
  N = int(input())
  print(n1[N-1]+n2[N-1]+n3[N-1])