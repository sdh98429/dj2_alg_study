# backtracking !! 부등호
# dfs 사용해서 해결
# 작은 숫자 찾을 때는 부등호 조건에 맞게 0부터 9까지 넣어보고, 큰 숫자 찾을 때는 부등호 조건에 맞게 9에서 0까지 넣어보기

def dfs(ind):
    global flag, select # 정답 찾았으면 무의미한 반복 없애는 flag, 현재 시도하는 행렬 select
    if flag: # 정답 찾았으면 끝
        return

    if ind == K: # 마지막 인덱스까지 도착시
        for k in range(K+1):
            print(select[k], end="")
        print() # 출력하고 flag True
        flag = True
        return

    for i in order: # order는 0~9 또는 9~0
        if not visited[i]: # 아직 안 쓴 숫자라면
            if S[ind] == "<": # 부등호 <일 때
                if select[ind] < i: # i가 직전 숫자보다 크다면 방문처리, select도 바꿔주고, 다시 dfs 빠져나오면 원상태로 복구
                    visited[i] = 1
                    select[ind+1] = i
                    dfs(ind+1)
                    select[ind+1] = 0
                    visited[i] = 0
            else:
                if select[ind] > i:
                    visited[i] = 1
                    select[ind+1] = i
                    dfs(ind+1)
                    select[ind+1] = 0
                    visited[i] = 0

K = int(input())
S = list(input().split())


small = [i for i in range(10)] # 작은 숫자 찾기
big = [i for i in range(9,-1,-1)] # 큰 숫자 찾기


for ord in [big, small]:
    visited = [0] * 10
    select = [0] * 10
    flag = False

    for j in ord: # 첫번째 숫자 골라주는 건 dfs 함수 외부에서 진행했다. 왜냐하면 dfs 함수 안에 넣으면 좀 안 예뻐보여서
        order = ord
        select[0] = j
        visited[j] = 1
        dfs(0)
        visited[j] = 0
