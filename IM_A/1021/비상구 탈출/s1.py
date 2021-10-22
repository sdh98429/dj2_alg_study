# 1번 비상구 탈출 01:31:16 100/100점
# 1번 비상구로 나올 때, 2번 비상구로 나올 때 시간 기록
def BFS(si, sj):
    global ind # 사람 번호
    q = [] 
    q.append((si, sj))
    visited[si][sj] = 1
    flag = 0 # 이미 도착했던 비상구 있는지 체크
    while q:
        vr, vc = q.pop(0)
        if vr == door[0][0] and vc == door[0][1]: # 1번 비상구 도착!
            out[0].append((ind, visited[vr][vc]-1)) # i번째 사람이 1번 비상구로 나갈 때 시간 기록
            if not flag: # 다른 비상구로 도착 안했다면 flag 1이 됨
                flag = 1
            else: # 다른 비상구도 도착했었으면 return
                return
        if vr == door[1][0] and vc == door[1][1]: # 2번 비상구 도착!
            out[1].append((ind, visited[vr][vc]-1))
            if not flag:
                flag = 1
            else:
                return

        for m in range(4): # 상하좌우 이동
            wr = vr + dr[m]
            wc = vc + dc[m]
            if wr in range(N) and wc in range(N) and not visited[wr][wc]:
                visited[wr][wc] = visited[vr][vc] + 1
                q.append((wr, wc))

# 모든 사람에 대해 1번 비상구로 나갔을 때와 2번 비상구로 나갔을 때 경우 다 따지기 (2^사람수) 사실 완전탐색...
def backtrack(lev, max_num, used1, used2): # lev는 사람 번호, max_num은 가장 늦은 탈출 시간, used1, 2는 1, 2번 비상구 이용ㅅ간
    global ans
    if lev == ind: # 마지막 사람까지 체크 끝!
        if ans > max_num: # 가장 늦은 탈출시간이 ans보다 빠르면 교체
            ans = max_num
        return

    t1 = out[0][lev][1] + 1 # lev번째 사람이 1번 비상구에서 빠져나올때 시간 t1 
    while used1[t1]: # 이미 t1에 누가 탈출했다면, 다음 차례로!
        t1 += 1
    used1[t1] = 1
    if t1 > max_num: # t1이 최대 소요시간보다 크면 바뀜
        max_num1 = t1
    else: # 아니라면 기존의 최대 소요시간과 같음
        max_num1 = max_num
    backtrack(lev+1, max_num1, used1, used2) # 다음 번째 사람 탐색
    used1[t1] = 0 # used는 돌려놓기

    t2 = out[1][lev][1] + 1
    while used2[t2]:
        t2 += 1
    used2[t2] = 1
    if t2 > max_num:
        max_num2 = t2
    else:
        max_num2 = max_num
    backtrack(lev+1, max_num2, used1, used2)
    used2[t2] = 0

# 하상우좌 이동
dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)

T = int(input()) # 테스트케이스

for tc in range(1, T+1):
    N = int(input()) # 맵 크기
    mat = [list(map(int, input().split())) for _ in range(N)] # 맵
    people = [] # 탈출할 사람들 위치
    door = [] # 비상구 위치
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1: # 탈출할 사람 발견
                people.append((i, j))
            elif mat[i][j] == 2: # 비상구 발견
                door.append((i, j))
    ind = 0 # 탈출할 사람 번째 수
    out = [[] for _ in range(2)] # 1번 비상구로 나가는 경우, 2번 비상구로 나가는 경우
    for si, sj in people: # 각각의 사람들에 대해 1번 비상구로 나갈 때와 2번 비상구로 나갈 때 시간 계산
        visited = [[0] * N for _ in range(N)]
        BFS(si, sj)
        ind += 1
    Used1 = [0] * 100 # 1번 비상구에서 사람들이 탈출하는 시간을 1로 바꿈
    Used2 = [0] * 100 # 2번 비상구에서 사람들이 탈출하는 시간
    ans = 987654321 # 전체 소요 시간
    backtrack(0, 0, Used1, Used2) # 모든 사람들에 대해 1, 2번 비상구로 나가는 경우 2^사람수 만큼 계산
    print('#{} {}'.format(tc, ans))



