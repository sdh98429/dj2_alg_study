# ! 위장, 딕셔너리
# 42578

def solution(clothes):
    
    fashion = dict() # 각 종류에 해당하는 옷의 개수
    
    for cloth in clothes:
        if fashion.get(cloth[1]): # 만약 종류가 이미 있다면 개수 늘리기
            fashion[cloth[1]] += 1
        else: # 종류 없다면 1로 시작
            fashion[cloth[1]] = 1
            
    answer = 1
    
    for f in fashion: # 안고르거나, 하나 고르거나의 경우
        answer *= (fashion[f]+1)
        
    return answer - 1 # 모두 안 고른 경우 빼주기

#     clothes	return
# [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	5
# [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]	3