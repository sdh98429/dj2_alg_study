# 64061
# 크레인 인형뽑기 게임

from collections import deque
stack = deque()

def solution(board, moves):
    N = len(board) # 보드 크기
    H = [N-1] * N # 최고 높이

    for i in range(N): # 각 열 최고 높이 찾기
        for j in range(N):
            if board[j][i]:
                H[i] = j
                break

    answer = 0

    for m in moves:
        if H[m-1] in range(N) and board[H[m-1]][m-1]: # 해당 m에 선물 존재하면
            if stack:
                doll = stack.pop()
                if board[H[m-1]][m-1] == doll: # 같은 종류
                    answer += 2
                else: # 다른 종류
                    stack.append(doll)
                    stack.append(board[H[m-1]][m-1])
            else:
                stack.append(board[H[m-1]][m-1])
            H[m-1] += 1 # 맨 위 선물 뺐으니 한 칸 아래로

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))