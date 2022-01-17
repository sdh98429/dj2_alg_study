# !! 신고 결과 받기
# 92334

def solution(id_list, report, k):
    answer = []
    user = {} # 신고 받은 사람 기준 신고한 사람
    result = {} # 신고한 사람 기준 유죄인 사람
    guilty = [] # 유죄인 사람 목록

    for r in report:
        good, bad = r.split()

        try:
            if good not in user[bad]: # 만약 동일한 사람이 한 신고가 아니라면
                user[bad].append(good)
        except: # 최초 신고
            user[bad] = [good]

    for id in id_list:
        try: # k개 이상 신고면 유죄
            if len(user[id]) >= k:
                guilty.append(id)
        except:
            pass

    for r in report:
        good, bad = r.split()
        if bad in guilty: # bad가 유죄고
            try: # 중복 신고가 아니라면
                if bad not in result[good]:
                    result[good].append(bad)
            except:
                result[good] = [bad]

    for i in range(len(id_list)): # 순서대로 신고했던 사람 중 유죄였던 사람 출력
        try:
            answer.append(len(result[id_list[i]]))
        except:
            answer.append(0)

    return answer

# id_list	report	k	result
# ["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	2	[2,1,1,0]
# ["con", "ryan"]	["ryan con", "ryan con", "ryan con", "ryan con"]	3	[0,0]