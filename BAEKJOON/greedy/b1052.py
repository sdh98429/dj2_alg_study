# greedy 물병, 다른 사람 코드 참고해서 겨우 풂
# 조합으론 실패, 이진법 비트마스킹으로 풀었으며 어려웠음
N, K = map(int, input().split())

tot = 0 # 더해줘야 하는 물병의 수
while True:
    cnt = 0 # 최소로 만들 수 있는 물병의 수
    for i in range(25, -1, -1): # 10 ^7 보다 2 ^25가 더 큼
        if N & (1 << i): # 이진수로 표현시 1이 존재하는지 확인
            cnt += 1 # 최소 물병의 수 1 추가
            plus = 1 << i # 더해줘야 하는 물병의 값
    if cnt <= K: # K 보다 작은 경우 전부 포함
        break
    else:
        N += plus # 물병의 값 더해주기
        tot += plus # 물병의 값 더해주기

print(tot)