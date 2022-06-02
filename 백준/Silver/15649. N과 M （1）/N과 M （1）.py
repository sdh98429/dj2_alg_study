N, M = map(int, input().split())

used = [False] * (N+1)
def back(m, p):
    global used
    if m == 0:
        print(*p)
        return
    for i in range(1, N+1):
        if not used[i]:
            used[i] = True
            back(m-1, p + [i])
            used[i] = False

back(M, [])