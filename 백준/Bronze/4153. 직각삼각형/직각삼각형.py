while True:
    S = list(map(int ,input().split()))
    if S[0] or S[1] or S[2]:
        S.sort()
        if S[2] ** 2 == S[1] ** 2 + S[0] ** 2:
            print('right')
        else:
            print('wrong')
    else:
        break