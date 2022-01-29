# 콜라츠 추측
# 12943

def solution(num):
    answer = 0
    while answer < 500:
        if num == 1:
            break
        if num%2:
            num = 3 * num + 1
        else:
            num //= 2
        answer += 1
    else:
        answer = -1
    return answer

# n	result
# 6	8
# 16	4
# 626331	-1