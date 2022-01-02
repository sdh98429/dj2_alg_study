# queue 크리스마스 선물

N = int(input())
have = []
for _ in range(N):
    pre = list(map(int, input().split()))
    if pre[0]:
        for p in pre[1:]:
            have.append(p)
        have.sort(reverse=True)
    else:
        if have:
            print(have.pop(0))
        else:
            print(-1)
