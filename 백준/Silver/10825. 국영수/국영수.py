import sys
input = sys.stdin.readline

N = int(input())
L = list()

for _ in range(N):
  Student = list(input().split())
  Student[1:4] = map(int, Student[1:4])
  L.append(Student)
L.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for l in L:
  print(l[0])