# OX 퀴즈

T = int(input())

for tc in range(1, T+1):
    S = list(input())
    ans = 0
    wgt = 1
    for s in S:
        if s == 'O':
            ans += wgt
            wgt += 1
        else:
            wgt = 1
    print(ans)