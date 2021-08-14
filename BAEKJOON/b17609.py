
# 회문 함수 작성
def palindrome(words): # 양쪽 끝에서 비교하며 미일치하는 부분이 나올 때 왼쪽에서 한칸 띄우고, 오른쪽에서 한칸 띄우고 다시 비교한다
    result = left = right = ind = 0 # 회문 결과값, 왼쪽, 오른쪽, 인덱스값
    while ind < len(words)//2: # 양쪽 끝부터 비교하므로 전체 길이의 절반
        if words[left + ind] != words[-right-ind-1]: # 왼쪽 끝과 오른쪽 끝 비교
            if not left and not result: # 처음 미일치하는 부분 발견
                miss = ind # 미일치한 인덱스 값 저장
                left = 1 # 왼쪽에서 미일치한 부분을 무시한다 dassa 라면 d를 무시
                result = 1 # 유사회문 결과값 1로 설정
            elif not right: # 왼쪽에서 미일치하는 부분을 무시하고 시행하다 다시 미일치 발견
                ind = miss # 이번엔 오른쪽에서 미일치한 부분을 무시하기 위해 인덱스 불러옴
                left = 0 # 오른쪽에서 미일치한 부분을 무시한다 assad 라면 d를 무시 
                right = 1
            else: # 3번째 미일치하는 부분 발견이면 회문도, 유사회문도 아님
                return(2)
            ind -= 1 # 왼쪽을 무시할지, 오른쪽을 무시할지 결정하고 미일치하는 부분 인덱스에서 다시 시작
        ind += 1
    return(result) # 결과 반환

T = int(input())

for tc in range(1, T+1):
    words = input()
    print(palindrome(words))