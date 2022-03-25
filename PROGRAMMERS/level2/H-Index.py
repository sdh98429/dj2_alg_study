# ! H-Index
# 42747

def solution(citations):
    citations.sort(reverse=True) # 큰 순서로 정렬
    for i in range(len(citations)):
        if i+1 > citations[i]:
            return i
    else: # 마지막까지 완료시
        return len(citations)

# citations	return
# [3, 0, 6, 1, 5]	3