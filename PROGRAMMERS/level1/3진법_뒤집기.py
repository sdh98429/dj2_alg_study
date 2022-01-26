# 3진법 뒤집기
# 68935

def solution(n):
    answer = 0
    three = ''
    while n:
        three = str(n%3) + three
        n //= 3
    for i in range(len(three)):
        answer += 3 ** i * int(three[i])
    return answer

# n	result
# 45	7
# 125	229