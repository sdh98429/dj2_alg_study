# !! [1차] 뉴스 클러스터링, 범위 조심
# 17677

def solution(str1, str2):
    str1 = str1.upper() # 전부 대문자로 변경
    str2 = str2.upper()

    L1 = list() # 중복 원소 안 없애므로 다중집합은 리스트로 표현
    L2 = list()
    
    for i in range(len(str1)-1): # 마지막-1
        if ord(str1[i]) in range(65, 91) and ord(str1[i+1]) in range(65, 91): # 범위 65, 90으로 잡았다 10, 11 예제 계속 틀림 주의하자
            L1.append(str1[i:i+2]) # 다중집합 요소 더하기

    for i in range(len(str2)-1): # 두번째 문자열
        if ord(str2[i]) in range(65, 91) and ord(str2[i+1]) in range(65, 91):
            L2.append(str2[i:i+2])


    inter = 0 # 중복원소 개수
    for l in L1:
        for i in range(len(L2)):
            if l == L2[i]: # 중복 원소 확인
                L2[i] = -1 # 문자열을 -1로 바꿔버리기
                inter += 1 # 중복 원소 개수 추가
                break # 다른 자리 안 건드리게
    if len(L1) + len(L2) - inter: # 0이 아니라면
        answer = int((inter / (len(L1) + len(L2) - inter)) * 65536)

    else: # 0이면 65536
        answer = 65536
    
    return answer

# str1	str2	answer
# FRANCE	french	16384
# handshake	shake hands	65536
# aa1+aa2	AAAA12	43690
# E=M*C^2	e=m*c^2	65536