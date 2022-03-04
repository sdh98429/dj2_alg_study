# ! 정수 내림차순으로 배치하기, int 형으로 변환 long
# 12933

def solution(n):
    # 처음에 n을 받을 때 int(n)으로 받지 않으면 범위문제로 long형 때문에 런타임 에러가 생긴다
    return int("".join(map(str, sorted(map(int, list(str(int(n)))), reverse=True))))
    # 다른 풀이
    # answer = ''
    # for i in sorted(list(str(int(n)))):
    #     answer = i + answer
    # return int(answer)

# 제한 조건
# n은 1이상 8000000000 이하인 자연수입니다.
# 입출력 예
# n	return
# 118372	873211