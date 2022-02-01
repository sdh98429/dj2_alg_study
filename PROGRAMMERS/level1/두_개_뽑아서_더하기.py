# 두 개 뽑아서 더하기
# 68664

def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i] + numbers[j])
    answer.sort()
    return answer

# numbers	result
# [2,1,3,4,1]	[2,3,4,5,6,7]
# [5,0,2,7]	[2,5,7,9,12]