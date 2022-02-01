# 문자열 압축 !! 1부터 최대 n//2만큼 자르기, 겹치는 개수 자리수 바뀌는 것 주의
# 60057

def solution(s):
    answer = len(s)
    
    for n in range(1, len(s)//2+1): # 자르는 길이 단위
        i = 0 # 인덱스
        flag = 0 # 연속해서 몇 개나 겹치는지 (2abc -> 3abc)
        now = len(s) # 현재 n 기준 잘리는 길이
        while i <= len(s)-2*n: # i:i+n과 i+n:i+2*n이 겹치는 지 확인
            if s[i:i+n] == s[i+n:i+2*n]:
                i += n # 겹치면 다음 n개 넘어감
                if flag: # 연속으로 겹치면 n개 빼기
                    now -= n
                else: # 처음 겹치는 거면 앞에 2 붙이니 n-1개 빼기
                    now -= n - 1
                flag += 1 # 겹치는 횟수 flag
                if len(str(flag)) < len(str(flag+1)): # 반복되는 수가 많아져 10x, 100x 등으로 자리수 변하면 1 더해주기
                    now += 1
            else:
                i += n # 안겹쳐도 다음 n개 넘어감 (처음 풀 때 앞에서부터 잘라야한다는 규칙 몰라서 원래는 1로 둠...)
                flag = 0 # 초기화
        if now < answer: # 최소 길이 찾기
            answer = now

    return answer

# s	result
# "aabbaccc"	7
# "ababcdcdababcdcd"	9
# "abcabcdede"	8
# "abcabcabcabcdededededede"	14
# "xababcdcdababcdcd"	17

# 앞에서부터 잘라야한다는 규칙 없을 때 풀던 과정
# def solution(s):
#     answer = len(s)
    
#     for n in range(1, len(s)//2+1):
#         i = 0
#         flag = False
#         now = len(s)
#         while i <= len(s)-2*n:
#             if s[i:i+n] == s[i+n:i+2*n]:
#                 # print(s[i:i+n])
#                 i += n
#                 if flag:
#                     now -= n
#                 else:
#                     now -= n - 1
#                 flag = True
#             else:
#                 i += 1
#                 flag = False
#         print(now)


#     return answer