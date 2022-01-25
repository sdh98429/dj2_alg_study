# 같은 숫자는 싫어
# 12906

def solution(arr):
    answer = [arr[0]]
    for a in arr:
        if a != answer[-1]:
            answer.append(a)
    return answer

# arr	answer
# [1,1,3,3,0,1,1]	[1,3,0,1]
# [4,4,4,3,3]	[4,3]