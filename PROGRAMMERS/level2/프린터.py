# !! 프린터, 중요도 sorted
# 42587

def solution(priorities, location):
    P = sorted(priorities, reverse=True) # 중요도 큰 순으로 배열
    
    ind = 0 # 현재 요청 문서
    p_ind = 0 # 다음으로 처리해야할 중요도 순서
    while p_ind < len(priorities): # 만약 다 사용하지 않았다면
        if priorities[ind] == P[p_ind]: # 만일 지금 문서가, 다음에 처리해야할 중요도와 같다면
            p_ind += 1 # 중요도 순서 + 1
            if ind == location: # 만약 location과 같다면 return 처리 번째 수
                return p_ind
        ind = (ind+1) % len(priorities) # 순환

# priorities	location	return
# [2, 1, 3, 2]	2	1
# [1, 1, 9, 1, 1, 1]	0	5