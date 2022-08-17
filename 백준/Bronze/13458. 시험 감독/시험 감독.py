N = int(input())
A = list(map(int ,input().split()))
B, C = map(int, input().split())

ans = 0
for a in A:
  if a >= B:
    ans += (a - B)//C + 2 if (a-B)%C else (a - B)//C + 1
  else:
    ans += 1
print(ans)