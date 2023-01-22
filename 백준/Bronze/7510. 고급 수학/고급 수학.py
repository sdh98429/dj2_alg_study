T = int(input())

for tc in range(T):
  S = list(map(int, input().split()))
  S.sort()
  if S[2] ** 2 == S[0] ** 2 + S[1] ** 2:
    print(f'Scenario #{tc+1}:')
    print('yes')
  else:
    print(f'Scenario #{tc+1}:')
    print('no')
  print()