# 완주하지 못한 선수
# 42576
# 동명이인 존재 가능

def solution(participant, completion):
    answer = ''
    participant.sort()  # 이름 순 정렬
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:  # 이름 순 정렬이 어긋났을 때가 미완주자
            answer = participant[i]
            break
    else:
        answer = participant[-1]  # 마지막 참가자가 미완주자

    return answer

# participant	completion	return
# ["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
# ["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
# ["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"