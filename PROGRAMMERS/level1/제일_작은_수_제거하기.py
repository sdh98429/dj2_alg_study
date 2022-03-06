# 제일 작은 수 제거하기
# 12935

def solution(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]

# arr	return
# [4,3,2,1]	[4,3,2]
# [10]	[-1]