# ! k진수에서 소수 개수 구하기
# 92335

def isPrime(n):
    if n > 1:
        for i in range(2, int(n**(1/2))+1):
            if not n%i:
                return False
        else:
            return True
    return False

def solution(n, k):
    answer = 0
    new = ''
    while n:
        new = str(n%k) + new
        n //= k
    new += '0'
    cand = ''
    for s in new:
        if s == '0':
            if cand and isPrime(int(cand)):
                answer += 1
            cand = ''
        else:
            cand += s
    return answer

# n	k	result
# 437674	3	3
# 110011	10	2