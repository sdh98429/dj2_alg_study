N = int(input())
Card = set(map(int ,input().split()))
M = int(input())
Test = list(map(int, input().split()))
for t in Test:
  if t in Card:
    print(1, end=" ")
  else:
    print(0, end=" ")