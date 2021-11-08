# MST ! 별자리 만들기
# KRUSKAL 사용

def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])

def union(x, y):
    p[find_set(y)] = find_set(x)

N = int(input())

AXIS = [[] for _ in range(N)]
p = [i for i in range(N)]

for i in range(N):
    AXIS[i] = list(map(float, input().split()))

EDGE = []

for i in range(N):
    for j in range(i+1, N):
        # 소수점 둘째 자리로 변환
        EDGE.append((float(format(((AXIS[i][0] - AXIS[j][0]) ** 2 + (AXIS[i][1] - AXIS[j][1]) ** 2) ** (1/2), '.2f')), i, j))

EDGE.sort()

tot = 0
cnt = 0
for eg in EDGE:
    W, n1, n2 = eg
    if find_set(n1) != find_set(n2):
        union(n1, n2)
        tot += W
        cnt += 1
        if cnt == N -1:
            break

print(tot)