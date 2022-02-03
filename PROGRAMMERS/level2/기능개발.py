# ! 기능개발
# 42586

def solution(progresses, speeds):
    answer = [0]
    que = []
    for i in range(len(progresses)):
        que.append((100-progresses[i])//speeds[i] +1 if (100-progresses[i])%speeds[i] else (100-progresses[i])//speeds[i]) # 깔끔하게 나눠지지 않을 때
    now = que[0] # 최장시간

    for i in range(len(que)):
        if not que[i] > now:
            answer[-1] += 1
        else:
            answer.append(1)
            now = que[i]
    return answer

# progresses	speeds	return
# [93, 30, 55]	[1, 30, 5]	[2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]