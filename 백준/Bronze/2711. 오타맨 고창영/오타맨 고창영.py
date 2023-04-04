import sys
input = sys.stdin.readline
T = int(input())

for tc in range(T):
  N, S = input().split()
  print(S[:int(N)-1]+S[int(N):])