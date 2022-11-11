import sys
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
L = list(map(int, input().split()))

def BinarySearch(A, l, start, end):
  if start > end:
    return 0
  mid = (start + end) // 2
  if l == A[mid]:
    return 1
  elif l < A[mid]:
    return BinarySearch(A, l, start, mid-1)
  else:
    return BinarySearch(A, l, mid+1, end)

for l in L:
  start = 0
  end = N-1
  print(BinarySearch(A, l, start, end))