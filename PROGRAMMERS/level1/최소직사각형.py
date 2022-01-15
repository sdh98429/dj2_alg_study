# 최소직사각형
# 86491

def solution(sizes):
    long = 0
    short = 0
    for (a, b) in sizes: # 긴 쪽을 long에 몰아준다
        if not a >= b:
            a, b = b, a
        if a > long:
            long = a
        if b > short: # 짧은 쪽 중 최대가 short가 됨
            short = b
    return long * short

# sizes	result
# [[60, 50], [30, 70], [60, 30], [80, 40]]	4000
# [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	120
# [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	133