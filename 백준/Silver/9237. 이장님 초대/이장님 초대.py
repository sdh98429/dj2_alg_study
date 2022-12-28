import sys
input = sys.stdin.readline

N = int(input())
T = list(map(int, input().split()))

T.sort(reverse=True)
for i in range(1, N+1):
  T[i-1] += i
print(max(T)+1)