# 두 정수 사이의 합
# 12912

def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b+1))

# a	b	return
# 3	5	12
# 3	3	3
# 5	3	12