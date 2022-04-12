# ! 점프와 순간 이동, 홀수를 짝수로
# 12980
# 짝수면 순간 이동, 홀수면 1 이동해서 짝수로 만들기

def solution(n):
    ans = 0
    
    while n:
        if n%2:
            n -= 1
            ans += 1
        else:
            n //= 2

    return ans

# N	result
# 5	2
# 6	2
# 5000	5