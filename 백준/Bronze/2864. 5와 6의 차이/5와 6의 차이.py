A, B = input().split()
min_A = ''
max_A = ''

min_B = ''
max_B = ''

for a in A:
  if a == '5' or a=='6':
    max_A = max_A + '6'
    min_A = min_A + '5'

  else:
    max_A = max_A + a
    min_A = min_A + a

for b in B:
  if b == '5' or b=='6':
    max_B = max_B + '6'
    min_B = min_B + '5'
  else:
    max_B = max_B + b
    min_B = min_B + b

print(int(min_A)+int(min_B), int(max_A)+int(max_B))