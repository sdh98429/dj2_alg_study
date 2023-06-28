T = int(input())

for tc in range(1, T+1):
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  A.pop(0)
  B.pop(0)
  A.sort(reverse=True)
  B.sort(reverse=True)
  for i in range(min(len(A), len(B))):
    if A[i] > B[i]:
      print('A')
      break
    elif A[i] < B[i]:
      print('B')
      break
  else:
    if len(A) > len(B):
      print('A')
    elif len(A) < len(B):
      print('B')
    else:
      print('D')
  