# !! 튜플, 딕셔너리 및 람다로 너무 복잡하게 풂
# 64065

def solution(string):
    a = '' # 숫자 확인
    D = dict() # 딕셔너리
    for s in string[1:-1]: # 따옴표 제외
        if s in ('}' , ',', '{'):
            if a: # 만약 숫자가 있다면
                if D.get(int(a)): # 이미 존재한다면 개수 더하기
                    D[int(a)] += 1
                else: # 없다면 새로 생성
                    D[int(a)] = 1
            a = ''
        else:
            a = a + s # 자리수 더하기
    answer = []
    for d in sorted(D.items(), key = lambda x : x[1], reverse = True): # 값(개수)으로 딕셔너리 아이템 정렬하기
        answer.append(d[0])

    return answer

# s	result
# "{{2},{2,1},{2,1,3},{2,1,3,4}}"	[2, 1, 3, 4]
# "{{1,2,3},{2,1},{1,2,4,3},{2}}"	[2, 1, 3, 4]
# "{{20,111},{111}}"	[111, 20]
# "{{123}}"	[123]
# "{{4,2,3},{3},{2,3,4,1},{2,3}}"	[3, 2, 4, 1]