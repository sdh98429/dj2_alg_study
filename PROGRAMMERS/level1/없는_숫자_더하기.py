# 86051
# 없는 숫자 더하기

def solution(numbers):
    answer = 45
    for n in numbers:
        answer -= n
    return answer

print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))