def Quad(x, y, n):
    before = L[x][y]

    flag = True
    for i in range(x, x+n):
        for j in range(y, y+n):
            if before != L[i][j]:
                flag = False
                break
    if flag:
        print(before, end="")
    else:
        n //= 2
        print('(', end="")
        Quad(x, y, n)
        Quad(x, y+n, n)
        Quad(x+n, y, n)
        Quad(x+n, y+n, n)
        print(')', end="")

N = int(input())

L = list(list(input()) for _ in range(N))

Quad(0, 0, N)