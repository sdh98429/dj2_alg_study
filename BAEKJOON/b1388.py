
N, M = list(map(int, input().split()))
mat = [list(input()) for _ in range(N)]

result = 0

for i in range(N):
    for j in range(M):
        if not i and mat[i][j] == '|':
            result += 1
            continue
        if not j and mat[i][j] == '-':
            result += 1
            continue
        if mat[i][j] == '|' and mat[i-1][j] == '|':
            continue
        elif mat[i][j] == '-' and mat[i][j-1] == '-':
            continue
        else:
            result += 1
print(result)

'''
# 다른 방식
def fence(ni, nj, shape):
    global path
    global result
    if ni >= N or nj >= M or path[ni][nj]:
        return
    if shape == 'start':
        path[ni][nj] = 1
        result += 1

    if mat[ni][nj] == '-':
        if not shape == '-':
            pass
        else:
            path[ni][nj] = 1
        fence(ni, nj + 1, '-')
    if mat[ni][nj] == '|':    
        if not shape == '|':
            pass
        else:
            path[ni][nj] = 1
        fence(ni + 1, nj, '|')

N, M = list(map(int, input().split()))
mat = [list(input()) for _ in range(N)]

path = [[0] * M for _ in range(N)]
result = 0

for i in range(N):
    for j in range(M):
        if path[i][j]:
            pass
        else:
            fence(i, j, 'start')
print(result)
'''