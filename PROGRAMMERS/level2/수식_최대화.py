# !!! 수식 최대화, 후위 계산 변환
# 67257

from itertools import permutations # 순열 라이브러리

def solution(expression):
    elems = [''] # 문자열 연산자와 피연산자로 바꾸기
    answer = 0 # 최대값
    
    for exp in str(expression):

        if ord(exp) not in range(48, 58): # 만약 0~9가 아니라면 연산자
            elems.append(exp) # 기존의 숫자 넣어주고 새로 시작
            elems.append('')
        else: # 0~9인 경우 피연산자, 뒤에 자리수 붙여주기 1 , 0 -> 10
            elems[-1] += exp

    ops = ['+', '-', '*'] # 연산자 종류
    for perm in list(permutations([i for i in range(3)])): # 원소의 개수가 3인 순열
        ops_ord = dict() # 우선순위 딕셔너리

        for i in range(3): # 정해진 우선순위 딕셔너리에 넣기
            ops_ord[ops[i]] = perm[i]
        
        post = [] # 후위 계산 순서
        stack = [] # 후위 계산 스택
        for elem in elems:
            if elem in ['*', '-', '+']: # 연산자일때
                while stack: # 스택이 남아있다면
                    if ops_ord[stack[-1]] >= ops_ord[elem]: # 우선순위가 같거나 높은 것들 전부 스택에서 빼서 post로 이동
                        post.append(stack.pop())
                    else: # 아니라면 while문 나오기
                        break
                stack.append(elem) # 연산자스택에 넣기
            else:
                post.append(elem) # 피연산자 post에 넣기
        
        while stack: # 아직 남아있는 스택의 연산자 이동
            post.append(stack.pop())
        
        p_stack = [] # 후위 계산용 스택
        for p in post:
            if p == '*': # 곱해주기
                p2, p1 = int(p_stack.pop()), int(p_stack.pop())
                p_stack.append(p1 * p2)
            elif p == '+': # 더해주기
                p2, p1 = int(p_stack.pop()), int(p_stack.pop())
                p_stack.append(p1 + p2)
            elif p == '-': # 빼주기, 나중에 pop된 p1으로부터 먼저 pop된 p2 빼주기
                p2, p1 = int(p_stack.pop()), int(p_stack.pop())
                p_stack.append(p1 - p2)
            else: # 피연산자 스택에 넣기
                p_stack.append(int(p))
        
        if abs(p_stack[0]) > answer: # 마지막 남은 스택, 즉 계산결과 최대인 것 찾기
            answer = abs(p_stack[0])
            
    return answer

# expression	result
# "100-200*300-500+20"	60420
# "50*6-3*2"	300