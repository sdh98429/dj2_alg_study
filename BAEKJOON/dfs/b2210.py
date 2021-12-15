# dfs 숫자판 점프
# 오랜만에 bfs 말고 dfs로 풀어보았다


def dfs(i, j, num, depth): # i, j 는 현재 좌표, num은 지금까지 쓴 숫자, depth는 몇 번째 이동인지 의미
    global six
    if depth == 6:
        if num not in six: # 겹치는 것 제외
            six.append(num)
        return

    for m in range(4): # 상하좌우 이동
        vi = i + di[m]
        vj = j + dj[m]
        if vi in range(5) and vj in range(5): # 범위 내라면 재귀
            dfs(vi, vj, num+pad[vi][vj], depth+1)


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

pad = [[] for _ in range(5)]

for i in range(5):
    pad[i] = list(input().split()) # int 대신 str 형태로 하면 편함

six = []

for i in range(5):
    for j in range(5):
        dfs(i, j, '', 0)

print(len(six))