# !! 체육복
# lost, reserve 겹치는 지 보고
# 순서대로 정렬해줘야 함
# remove 사용해도 풀림
# 42862

def solution(n, lost, reserve):
    spare = [False] * (n + 1)

    Lost = []
    Reserve = []

    for l in lost:
        if l not in reserve:
            Lost.append(l)
    Lost.sort()
    for r in reserve:
        if r not in lost:
            Reserve.append(r)

    answer = n - len(Lost)

    for r in Reserve:
        spare[r] = True

    for l in Lost:
        for i in range(-1, 2):
            if (l + i) in range(n + 1) and spare[l + i]:
                spare[l + i] = False
                answer += 1
                break

    print(spare)
    return answer

# n	lost	reserve	return
# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	4
# 3	[3]	[1]	2