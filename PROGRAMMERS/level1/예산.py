# 예산
# 12982

def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if budget >= i:
            budget -= i
            answer += 1
        else:
            break
    return answer

# d	budget	result
# [1,3,2,5,4]	9	3
# [2,2,3,3]	10	4