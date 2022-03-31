# !! 모음사전, 점화식 dfs
# 84512
# trial & error 식의 풀이긴 했습니다

D = dict() # 글자를 인덱스화
D['A'] = 1
D['E'] = 2
D['I'] = 3
D['O'] = 4
D['U'] = 5
answer = 0 # 번째수

def dfs(i, ind, first): # 점화식 dfs, i 글자, ind 현재 자릿수, first로 자기보다 작은 자리수 모두 합쳤는지 판별
    global answer
    if ind == 5: # 6번째 자릿수인 경우 0 return
        return 0
    if first: # 가장 바깥쪽 연산
        return (D[i]-1) * dfs(i, ind+1, 0) + D[i] # 가장 바깥 자릿수가 변하는 경우 아래의 모든 경우 + 현재 자릿수 하나만 있는 경우
    else: # a, e, i, o, u 5개 * (아래 자릿수의 모든 경우) + 현재 자릿수 하나만 있는 경우 * 5
        return 5 * dfs(i, ind+1, 0) + 5

def solution(word):
    global answer
    for ind, w in enumerate(word):
        answer += dfs(w, int(ind), 1) # dfs로 각 자릿수별 계산
    return answer

# word	result
# "AAAAE"	6
# "AAAE"	10
# "I"	1563
# "EIO"	1189