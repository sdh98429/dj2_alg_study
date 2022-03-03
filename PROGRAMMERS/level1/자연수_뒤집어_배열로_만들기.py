# 자연수 뒤집어 배열로 만들기
# 12932

def solution(n):
    answer = []
    for i in range(len(str(n))-1, -1, -1):
        answer.append(int(str(n)[i]))
    return answer

# n	return
# 12345	[5,4,3,2,1]