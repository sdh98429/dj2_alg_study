# 약수의 개수와 덧셈
# 77884

def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        answer += n if n ** (1/2) % 1 else - n # 제곱수일 때만 뺼셈
    return answer

# left	right	result
# 13	17	43
# 24	27	52