# 나머지가 1이 되는 수 찾기
# 87389

def solution(n):
    for i in range(2, n):
        if not (n-1)%i:
            return i

# n	result
# 10	3
# 12	11