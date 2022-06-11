A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    ans = A//(C-B) + 1
    print(ans)