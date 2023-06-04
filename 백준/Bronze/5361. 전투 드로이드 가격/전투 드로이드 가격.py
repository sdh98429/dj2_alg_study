T = int(input())

for tc in range(1, T+1):
  A, B, C, D, E = map(int, input().split())
  value = A*350.34 + B* 230.90+ C*190.55 + D*125.30 + E*180.90
  print('$', '%.2f'%value, sep="")