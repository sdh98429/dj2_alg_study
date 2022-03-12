# x만큼 간격이 있는 n개의 숫자
# 12954

def solution(x, n):
    return [x*i for i in range(1, n+1)]

# x	n	answer
# 2	5	[2,4,6,8,10]
# 4	3	[4,8,12]
# -4	2	[-4, -8]