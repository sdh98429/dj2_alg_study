# !! 주차 요금 계산, dict에 마지막 시간, 누적 시간
# 92341

def solution(fees, records):
    book = dict()
    answer = []
    for record in records:
        now_time, ID, move = record.split() # 현재 시간, 차 번호, in/out
        hour, minute = now_time.split(':') # 시간, 분
        now_time = int(hour) * 60 + int(minute) # 현재 시간 분으로
        if book.get(ID): # 만약 이미 dict에 있다면
            if move == 'OUT': # 나간다면
                last_time = book[ID][0] # 마지막으로 들어온 시간
                book[ID][1] += now_time - last_time # 현재 시간 - 마지막 시간을 누적 시간에 더한다
                book[ID][0] = -1 # 들어온 시간이 00:00일 때를 대비해 -1로 초기화

            else: # 들어온다면
                book[ID][0] = now_time
        else: # 처음 dict가 생기는 거면
            book[ID] = [now_time, 0] # 차량번호 등록, 현재 시간 및 누적 시간
    
    for ID in book: # 모든 차량 번호에 대해
        if book[ID][0] != -1:  # -1로 초기화 되어있지 않으면 23:59에 나간 것
            book[ID][1] += 60 * 23 + 59 - book[ID][0] # 23:59까지 누적 시간 추가
            
    for ID in sorted(book): # 차량 번호 작은 것부터
        if fees[0] >= book[ID][1]: # 기본 시간 내에 나감
            answer += [fees[1]]
        else: # 기본 시간 초과, 나머지 있을 때와 없을 때
            answer +=  [((book[ID][1]-fees[0])//fees[2])*fees[3] +fees[1]] if not (book[ID][1]-fees[0])%fees[2] else  [((book[ID][1]-fees[0])//fees[2]+1)*fees[3]+fees[1]]

    return answer

# fees	records	result
# [180, 5000, 10, 600]	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	[14600, 34400, 5000]
# [120, 0, 60, 591]	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	[0, 591]
# [1, 461, 1, 10]	["00:00 1234 IN"]	[14841]