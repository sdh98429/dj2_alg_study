
from itertools import combinations

N = int(input())
H = [i for i in range(N)]
C = combinations(H, N//2)
S = [list(map(int, input().split())) for _ in range(N)]
min_diff = 987654321


for c in C:
  T1 = list(c)
  T2 = [t for t in H if t not in T1]
  
  T1_C = combinations(T1, 2)
  T2_C = combinations(T2, 2)

  T1_score = 0
  T2_score = 0
  
  for t1_c in T1_C:
    h1, h2 = t1_c
    T1_score += S[h1][h2] + S[h2][h1]

  for t2_c in T2_C:
    h1, h2 = t2_c
    T2_score += S[h1][h2] + S[h2][h1]

  diff = abs(T1_score - T2_score)
  if min_diff > diff:
    min_diff = diff

  
print(min_diff)
