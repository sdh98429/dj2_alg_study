# !! 124 나라의 숫자, 3진법과 다름
# 12899

def solution(n):
    answer = ''
    
    while n > 3:
        answer = '124'[(n-1)%3] + answer
        n = (n-1)//3
    answer = '124'[(n-1)%3] + answer
    return answer

# 10진법	124 나라	10진법	124 나라
# 1	1	6	14
# 2	2	7	21
# 3	4	8	22
# 4	11	9	24
# 5	12	10	41