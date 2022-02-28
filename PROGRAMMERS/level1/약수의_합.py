# 약수의 합
# 12928

def solution(n):
    answer = 0
    if n:
        for i in range(1, int(n**1/2)+1):
            if not n%i:
                answer += i
        answer += n
    return answer

# n	return
# 12	28
# 5	6