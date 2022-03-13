# 타겟 넘버, dfs
# 43165

answer = 0

def plus(index, tot, numbers, target):
    global answer
    if index == len(numbers):
        if tot == target:
            answer += 1
        return
    else:
        plus(index+1, tot+numbers[index], numbers, target)
        plus(index+1, tot-numbers[index], numbers, target)
            
def solution(numbers, target):
    global answer
    plus(0, 0, numbers, target)
    return answer

# numbers	target	return
# [1, 1, 1, 1, 1]	3	5
# [4, 1, 2, 1]	4	2