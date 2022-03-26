# !!! 큰 수 만들기
# 10번 테스트 케이스 실행시간 초과가 아주 어려웠음
# 9일 때는 최대값 찾기 break으로 해결
# 42883

# 10번 실행 속도 줄이기, 단순히 max 사용하면 시간 초과
def solution(number, k):
    ind = 0 # number에서 인덱스
    answer = []
    while k and ind < len(number): # 만약 제거할 숫자가 남고 현재 인덱스가 전체 길이를 초과하지 않았다면
        max_n = '0' # 이번 범위에서 최대값
        move = 0 # 다음 검사를 시작하려 이동하는 값
        for i in range(len(number[ind:ind+k+1])): # 현재 인덱스에서 k 범위만큼 중에서 최대값 찾기
            if number[ind+i] == '9': # 10번 테스트케이스에서 아주 중요! 9로만 이루어진 경우에 시간 절감
                move = i # 만약 9를 찾았다면 최대값 찾기는 끝! i만큼 다음으로 이동해준다
                break # 최대값 찾는 for문 나가기
            if number[ind+i] > max_n: # 지금 숫자가 이번 범위 최대값을 넘을 때
                max_n = number[ind+i] # 최대값 바꾸기
                move = i # i만큼 이동해서 다음 최대값 찾을 준비
        answer.append(number[ind+move]) # 현재 범위의 최대값을 answer에 넣는다
        k -= move # 이동하는 범위만큼 숫자 제거
        ind += move + 1 # move만큼 이동한 다음에 시작하는 인덱스

    if not k: # k개 만큼 모두 제거했다면
        answer.append(number[ind:]) # 뒤에 남은 숫자만큼 그대로 이어붙이기 
    else: # 인덱스는 마지막까지 도달했지만, 제거할 숫자가 아직 남았다면
        answer = answer[:-k] # 남은 k개만큼 뒤에서 제거하기 ex. '654321' '2'라면 6543 
    return ''.join(answer) # answer를 문자열로 변환

# number	k	return
# "1924"	2	"94"
# "1231234"	3	"3234"
# "4177252841"	4	"775841"