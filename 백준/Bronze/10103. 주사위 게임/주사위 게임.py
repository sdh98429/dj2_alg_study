T = int(input())

score = [100] * 2

for tc in range(T):
  A, B = map(int, input().split())
  if A>B:
    score[1] -= A
  elif A<B:
    score[0] -= B

print(score[0])
print(score[1])