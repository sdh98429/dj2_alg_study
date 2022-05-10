# ! 수 정렬하기 3, N이 커서 sys 사용

import sys

N = int(sys.stdin.readline().rstrip())
L = [0] * 10001
for i in range(N):
    L[int(sys.stdin.readline().rstrip())] += 1

for i in range(1, 10001):
    for _ in range(L[i]):
        print(i)