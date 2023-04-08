import sys
input = sys.stdin.readline

A, B = input().split()

tot = 0

for i in range(len(A)):
  for j in range(len(B)):
    tot += int(A[i]) * int(B[j])
print(tot)