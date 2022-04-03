# 최솟값 만들기
# 12941

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer

# A	B	answer
# [1, 4, 2]	[5, 4, 4]	29
# [1,2]	[3,4]	10