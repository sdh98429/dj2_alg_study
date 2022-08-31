from itertools import permutations
N = int(input())
A = list(map(int, input().split()))

BruteForce = list(permutations(A, len(A)))
max_result = 0

for Brute in BruteForce:
  result = 0
  for i in range(N-1):
    result += abs(Brute[i] - Brute[i+1])
  if result > max_result:
    max_result = result
print(max_result)