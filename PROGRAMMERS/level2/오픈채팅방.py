# ! 오픈채팅방 - 딕셔너리 사용
# 42888

def solution(record):
    answer = []
    name = dict() # 이름 딕셔너리로 찾는 것이 젤 편함

    for r in record:
        rec = r.split() # 명령어, 아이디, 이름
        if not name.get(rec[1]): # 처음 보는 아이디
            name[rec[1]] = rec[2] # 아이디-이름 생성
        elif rec[0] in ('Change', 'Enter'): # 닉네임 변경 외에 다른 닉넴으로 새로 들어온 경우
            name[rec[1]] = rec[2] # 아이디-이름 변경
    
    for r in record:
        rec = r.split()
        if rec[0] == 'Enter': # 들어오는 경우
            answer.append(name[rec[1]] + "님이 들어왔습니다.")
        elif rec[0] == 'Leave': # 나가는 경우
            answer.append(name[rec[1]] + "님이 나갔습니다.")
    return answer

#     record	result
# ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]