import sys
input = sys.stdin.readline

N, M = map(int, input().split())
six_min = 987654321
one_min = 987654321

for _ in range(M):
  six, one = map(int, input().split())
  if six_min > min(six, 6*one_min):
    six_min = min(six, 6*one_min)
  if one_min > one:
    one_min = one

print(min(N//6 * six_min + N%6 * one_min, (N//6+1) * six_min, N * one_min))