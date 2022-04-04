# ! 다음 큰 숫자, 오른쪽에서 찾아가기
# 오른쪽에서 찾아가며 1을 만났었고, 그 왼쪽에 0이 있으면 교환
# 교환 전까지 만났던 1들은 전부 맨 오른쪽에 몰아두기
# 01001110 > 01010011
# 12911

def solution(n):
    binary = '0' + bin(n)[2:] # 이진수 변환
    one = 0 # 옮길 1의 위치
    isOne = False # 지금까지 1을 만났었는지
    move = False # 자리변경을 했는지
    answer = 0
    for i in range(len(binary)-1, -1, -1): # 오른쪽에서 찾아가기
        if binary[i] == '1': # 1인 경우
            isOne = True # 1을 만났다고 처리하기
            if move: # 만약 자리변경했다면
                answer += 2 ** (len(binary) - 1 - i) # 그냥 자리수에 맞게 바로 더해주기
            else: # 자리변경안했다면
                one += 1 # 지금까지 만난 1의 수 더하기
        else: # 0인 경우
            if isOne and not move: # 1을 만났고 자리변경안했다면 자리변경하기
                move = True # 자리변경 확인
                answer += 2 ** (len(binary) - 1 - i) # 0을 1로 바꾸기
                answer += 2 ** (one-1) -1 # 지금까지 만난 1 전부 오른쪽에 몰기
    return answer

# n	result
# 78	83
# 15	23