# ! 영어 끝말잇기
# 12981

def solution(n, words):
    D = dict() # 사용한 단어 딕셔너리 저장
    ind = 1 # 현재 사람
    seq = 1 # 현재 횟수
    last = words[0][0] # 마지막 단어의 마지막 글자
    
    for word in words: # 글자들
        if last != word[0]: # 끝말잇기가 이어지지 않았다면
            answer = [ind, seq] # 사람 번호와 횟수
            break
        last = word[-1] # 마지막 글자 업데이트
        
        if D.get(word): # 만약 이미 썼던 단어라면 끝
            answer = [ind, seq]
            break
        else:
            D[word] = 1 # 썼던 단어 새로 등록
            
        if ind == n: # 마지막 사람 번호라면
            seq += 1 # 횟수 증가
        ind = ind%n + 1 # 사람 번호 증가
    else: # 끝말잇기 성공
        answer = [0, 0] 

    return answer

# n	words	result
# 3	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	[3,3]
# 5	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]	[0,0]
# 2	["hello", "one", "even", "never", "now", "world", "draw"]	[1,3]