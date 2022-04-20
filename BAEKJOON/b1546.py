# 평균
N = int(input())

S = list(map(int, input().split()))

print(sum(S)/(max(S)*N)*100)