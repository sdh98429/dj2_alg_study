# 실패율
# 42889

def solution(N, stages):
    answer = []
    used = [0] * (N + 1)
    amount = [0] * (N + 2)
    user = [0] * (N + 1)

    for stage in stages:
        amount[stage] += 1

    for i in range(N, -1, -1):
        user[i] = (amount[i] / sum(amount[i:])) if sum(amount[i:]) else 0  # 0으로 나누지 않게

    while sum(used) < N:
        max_num = 0
        for i in range(N, 0, -1):
            if user[i] >= max_num and not used[i]:
                max_num = user[i]
                next = i
        used[next] = 1
        answer.append(next)

    return answer

# N	stages	result
# 5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
# 4	[4,4,4,4,4]	[4,1,2,3]