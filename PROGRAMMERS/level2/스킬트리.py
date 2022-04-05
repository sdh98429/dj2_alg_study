# ! 스킬트리, 딕셔너리
# 49993

def solution(skill, skill_trees):
    answer = 0
    D = dict() # 각 글자가 몇번째 위치에 있는지
    for i in range(len(skill)):
        D[skill[i]] = i # 각 스킬의 인덱스

    for skill_tree in skill_trees: # 모든 스킬트리에 대해
        ind = 0 # 인덱스 0으로 시작
        for tree in skill_tree: # 이 스킬트리에 대해
            if D.get(tree) == ind: # 만약 딕셔너리에 등록되어 있고, 인덱스가 일치한다면
                ind+=1 # 인덱스 + 1
            elif D.get(tree): # 딕셔너리에 등록만 되어있다면
                break # 인덱스가 틀렸으므로 break
        else: # 완료시 조건 만족
            answer += 1
    return answer

# skill	skill_trees	return
# "CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2