# 수 정렬하기 2

import sys

N = int(sys.stdin.readline().rstrip())
L = [0] * 2000001
for i in range(N):
    L[int(sys.stdin.readline().rstrip()) +1000000] += 1

for i in range(2000001):
    for _ in range(L[i]):
        print(i-1000000) 