# ! 연속합, 지금까지의 합이 음수면 버리기

N = int(input())
S = list(map(int, input().split()))

tmp = 0 # 현재까지 합
big = max(S) # 현재까지 최대합 (1개인 경우)

if big <= 0: # 모든 원소가 음수면 최대인 음수 고르기
    print(big)
else:
    for s in S: # 모든 원소에 대해
        if tmp + s >= 0: # 지금 원소 더해도 양이라면 지금 합 가져가기
            tmp += s
        else: # 지금 원소 더해서 음이라면
            tmp = 0 # 버리고 0에서 새로 시작하는 것이 낫다
        if big < tmp: # 만약 최대합보다 현재합이 크다면 바꾸기
            big = tmp
    print(big)
