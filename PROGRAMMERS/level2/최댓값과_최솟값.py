# 최댓값과 최솟값
# 12939

def solution(s):
    S = list(map(int, s.split()))
    big = S[0]
    small = S[0]
    for i in S:
        if i > big:
            big = i
        if i < small:
            small = i
    answer = str(small) + ' ' + str(big)
    return answer

# s	return
# "1 2 3 4"	"1 4"
# "-1 -2 -3 -4"	"-4 -1"
# "-1 -1"	"-1 -1"