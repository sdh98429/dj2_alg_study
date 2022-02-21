# 서울에서 김서방 찾기
# 12919

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            answer = '김서방은 ' + str(i) + "에 있다"
            break
    return answer

# seoul	return
# ["Jane", "Kim"]	"김서방은 1에 있다"