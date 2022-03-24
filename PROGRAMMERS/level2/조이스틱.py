# !!! 조이스틱, 그리디가 아니라 브루트 포스
# greedy로 해결하려다 실패, 양 옆 거리 같은 경우만 dps로 풀려다 실패
# 42860

min_move = 987654321 # 양 옆으로 최소 이동 거리

def LR(notA, ind, answer, name, para): # 가야하는 위치, 현재 위치, 이동 거리, 만들어야하는 단어, 디버깅 용 위치
    global min_move
    if notA: # 만약 아직 가야하는 위치가 남아있다면
        AR = min(abs(notA[0]-ind), len(name) - abs(notA[0]-ind))
        AL = min(abs(notA[-1]-ind), len(name) - abs(notA[-1]-ind))

        LA = notA.copy() # 왼쪽 이동 시 pop을 고려할 때 copy가 편함
        RA = notA.copy() # 오른쪽 이동 시

        ind = LA[-1] # 맨 오른쪽 A가 아닌 글자 자리로 이동
        LA.pop() # 맨 오른쪽 글자 처리
        LR(LA, ind, answer+AL, name, 'L') # 왼쪽으로 가기

        ind = RA[0] # 맨 왼쪽 A가 아닌 글자 자리로 이동
        RA.pop(0) # 맨 왼쪽 글자 처리
        LR(RA, ind, answer+AR, name, 'R') # 오른쪽으로 가기

    else: # 모든 A가 아닌 글자 위치로 이동 시
        if answer < min_move: # 최소 이동 수보다 작은 경우 최소값 바꾸기
            min_move = answer

def solution(name):
    answer_word = 0 # A를 해당하는 글자로 바꾸는데 소요되는 조작수
    notA = [] # A가 아닌 글자의 위치
    
    for i in range(len(name)):
        if name[i] != 'A':
            notA.append(i) # A가 아닌 글자의 위치 더하기
        
        answer_word += min(ord(name[i]) - 65, 91 - ord(name[i])) # A->Z 방향 이동 or Z->A 방향 이동
    
    ind = 0 # 시작 위치
    LR(notA, 0, 0, name, 'O') # A가 아닌 모든 위치를 갈 때 최소값 구하기 (ex 좌 우 좌, 우 좌 좌 등)
        
    return answer_word + min_move # 글자 변형에 소요되는 시행횟수 + 커서 위치 변경 시행횟수

# 65 90

# name	return
# "JEROEN"	56
# "JAN"	23