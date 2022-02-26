# !! 소수 찾기, 에라토노스의 체
# 12921

def solution(n):
# 시간 초과 함수, 제곱근까지만 소수 탐색 후 에라토노스의 체 하면 되었을 것
#     answer = 0
#     no_prime = [i for i in range(2, n+1)]

#     while no_prime:
#         p = sorted(list(no_prime))[0]

#         mul = set([m for m in range(p, n+1, p)])
#         no_prime = set(no_prime) - mul
#         answer += 1

    isPrime = [True] * (n+1) # 소수 판별 행렬
    answer = 0
    
    for p in range(2, int(n**1/2)+1): # 에라토노스의 체로 판별할 범위는 제곱근까지, 왜냐하면 100에서 11을 체로 거르려 한다면 121로 범위 초과
        if isPrime[p]: # 소수라면
            for m in range(p*2, n+1, p): # n까지 체로 거르기
                isPrime[m] = False
    
    for i in range(2, n+1): # 만약 소수라면 답에 1 더해줌
        answer += 1 if isPrime[i] else 0
        

    return answer

# n	result
# 10	4
# 5	3