N, B = map(int, input().split())
ans = ''

while N:
  if N%B < 10:
    ans = str(N%B) + ans
  else:
    ans = chr(N%B+55) + ans
  N = (N-N%B)//B
print(ans)