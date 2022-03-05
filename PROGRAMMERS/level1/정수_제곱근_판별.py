# 정수 제곱근 판별
# 12934

def solution(n):
    if not (n**0.5)%1:
        return int(((n**0.5)+1)**2)
    else:
        return -1

# n	return
# 121	144
# 3	-1