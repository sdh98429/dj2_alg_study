# 나누어 떨어지는 숫자 배열
# 12910

def solution(arr, divisor):
    answer = []
    arr.sort()
    for a in arr:
        if not a%divisor:
            answer.append(a)
    return answer if answer else [-1]

# arr	divisor	return
# [5, 9, 7, 10]	5	[5, 10]
# [2, 36, 1, 3]	1	[1, 2, 3, 36]
# [3,2,6]	10	[-1]