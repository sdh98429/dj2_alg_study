# 최대공약수와 최소공배수
# 12940

def solution(n, m):
    div = 1
    for i in range(1, int(n**(1/2)+1)): # 약수 제곱근까지만 탐색
        if not n%i: # i 가 n의 약수
            if not m%i: # i가 m의 약수
                if i > div:
                    div = i
            if not m%(n//i): # n//i가 m의 약수
                if n//i > div:
                    div = n//i
    return [div, m * n // div]

# n	m	return
# 3	12	[3, 12]
# 2	5	[1, 10]