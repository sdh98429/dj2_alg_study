# 핸드폰 번호 가리기
# 12948

def solution(phone_number):
    return "*"*(len(phone_number)-4)+phone_number[-4:]

# phone_number	return
# "01033334444"	"*******4444"
# "027778888"	"*****8888"