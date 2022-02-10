# !! 더 맵게, 시간초과 코드
# 42626

def solution(scoville, K):
    scoville.sort(reverse=True)

    answer = 0

    while scoville[-1] < K:
        if len(scoville) == 1:
            answer = -1
            break
        answer += 1
        a = scoville.pop()
        b = scoville.pop()
        scoville.append(a + b * 2)
        scoville.sort(reverse=True)
        
    return answer

# scoville	K	return
# [1, 2, 3, 9, 10, 12]	7	2