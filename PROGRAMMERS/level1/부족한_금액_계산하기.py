# 부족한 금액 계산하기
# 82612

def solution(price, money, count):
    answer = money - price * (1+count) * count // 2
    return -answer if answer < 0 else 0

# price	money	count	result
# 3	20	4	10