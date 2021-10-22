# 2번 업무 완료하기 02:20:11 72/100점 오답!

# 바로 시작할 수 있는 업무부터 시작해서 끝나는 시간 계산하고,
# 그렇게 끝난 업무들로 인해 새로 시작할 수 있는 업무 있으면 그것들도 계산 반복
def work():
    global flag, ans # flag는 업무 절대 못 끝내는 경우, ans는 최소 시간
    finish = [0] * (N+1) # 업무들이 끝나는 시간
    start = [] # 시작할 수 있는 업무들
    f_list = [] # 이미 끝난 업무들
    cnt = 0 # 완료한 업무의 개수
    while cnt != N: # 아직 업무가 남아있다!
        for i in range(1, N+1):
            if i in f_list: # 이미 끝낸 업무는 고려 안함
                continue
            if not task_list[i]: # task_list가 비어있으면, 즉 어떤 사전 업무도 필요 없다면
                start.append((0, i)) # start에 업무 시작 시간 0, 하는 업무 번호 i 기록
            else: # 사전에 끝내야하는 업무가 있다면
                f_time = 0 # 사전 업무가 마지막으로 끝난 시간
                for f in task_list[i]: # 사전에 끝내야 하는 업무들 중
                    if f in f_list: # 사전에 끝난 업무가 들어있다면
                        if f_time < finish[f]: # 가장 마지막에 끝난 시간부터 시작해주면 된다
                            f_time = finish[f]
                    else: # 아직 못 끝낸 업무가 있다면 빠져나오기
                        break
                else: # break 문 안타고 사전 업무 전부 완료한 상태면 시작할 수 있는 업무에 넣어줌
                    start.append((f_time, i))

        if not start: # 남은 업무 중 새로 시작할 수 있는 업무 없으면 나오기
            flag = 1
            return

        while start: # 시작할 수 있는 업무 남아있으면
            s_time, s_ind = start.pop(0) # 시작 시간, 업무 번호
            finish[s_ind] = s_time+task[s_ind][0] # 마지막으로 끝난 사전 업무 시간 + 현재 업무시간 소요량 
            f_list.append(s_ind) # 끝난 업무에 추가
            cnt += 1 # 끝난 업무 개수 추가

    if max(finish) < ans: # ans보다 일찍 끝났으면 ans 바꾸기
        ans = max(finish)

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 업무 개수
    task = [[]] +[list(map(int, input().split())) for _ in range(N)] # 업무 시간, 사전 업무 개수, 사전 업무 종류
    task_list = [[] for _ in range(N+1)] # 각각의 업무에 대한 사전 업무
    for i in range(1, N+1):
        for j in range(2, len(task[i])):
            task_list[i].append(task[i][j]) 
    flag = 0 # 업무 전체를 마치는게 불가능한지
    ans = 987654321 # 최소 소요 시간
    for i in range(1, N+1): # 각각의 업무에 수석을 붙여서 시간 비교
        tmp = task[i][0] # tmp에 수석 붙이기 전 시간 기록
        task[i][0] //= 2 # 수석 붙이기
        work()
        task[i][0] = tmp
    if flag: # 답이 없음
        ans = -1
    print('#{} {}'.format(tc, ans))

