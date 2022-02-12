# ! 짝지어 제거하기, 스택 얕은 복사
# 12973

def solution(s):
    stack = []
    while len(stack) != len(s): # 길이가 변하지 않는다면 return 0
        for i in s:
            if not stack: # 만약 stack이 비었다면 하나 추가
                stack.append(i)
            else:
                p = stack.pop() # stack pop
                if p != i: # 새로 추가하는 요소가 스택의 맨 위와 다르면 추가
                    stack.append(p)
                    stack.append(i)
        s = stack.copy() # s = stack일시 for 문 중간에 길이 변동으로 런타임 에러
        
    return 0 if stack else 1 # 스택이 남은 경우 0, 다 쓴 경우 1


# s	result
# baabaa	1
# cdcd	0