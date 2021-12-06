# greedy 온라인 판매
# 내림차 순 정렬해서 합이 최대보다 커질 때 갱신
# 계란 최대 수 고려해주기
# if 뒤에 else break 하면 오답처리 됨, 모든 경우의 수를 거쳐야함


N, M = map(int, input().split())
egg = []
for _ in range(M):
    egg.append(int(input()))
egg.sort(reverse=True)

price = 0
ans = 0
for i in range(M):
    if (i+1) * egg[i] >= ans and (i+1) <= N:
        ans = (i+1) * egg[i]
        price = egg[i]
print(price, ans)
