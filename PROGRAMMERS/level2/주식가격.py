# !! 주식가격, enumerate 스택
# 42584

def solution(prices):
    answer = [0] * len(prices) # 초 단위 주식가격에서 가격이 떨어지지 않은 기간
    stack = [] # (시간, 가격) 순으로 쌓인 스택
    for time, price in enumerate(prices): # 시간, 가격
        while stack: # 만약 stack이 있다면
            s_time, s_price = stack.pop() # 맨 위의 시간과 가격
            if s_price > price: # 만약 과거의 가격이 지금보다 높다면, 즉 가격이 떨어졌다면
                answer[s_time] = time - s_time # 해당 과거 시간에서 (지금 시간-과거 시간) 등록
            else: # 가격이 안 떨어졌다면
                stack.append((s_time, s_price)) # 다시 채워넣고 break
                break
        stack.append((time, price)) # 현재 시간과 가격 스택에 쌓기
    
    for s_time, s_price in stack: # 아직 stack이 남아있다면, 즉 끝까지 가격이 안 떨어졌다면
        answer[s_time] = len(prices) - 1 - s_time # 마지막 시간 - 과거 시간 등록
    
    return answer

# prices	return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]