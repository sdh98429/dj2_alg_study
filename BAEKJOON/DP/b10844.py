# ! 쉬운 계단 수

N = int(input())

last = [[0] * 10 for _ in range(N)] # 각 끝자리 수가 0~9인 계단수의 수

last[0] = [0] + [1] * 9 # 한자리수 계단수의 경우 0을 제외하고 1~9

for i in range(1, N):
    for j in range(10): # 각 끝 자릿수에 대해
        last[i][j] = (last[i-1][j-1] if j >0 else 0) + (last[i-1][j+1] if j < 9 else 0) # 길이가 i인 계단수이고 끝자리가 j라면 i-1번째 계단수의 j-1, j+1 끝자리의 합이다. (0, 9는 1과 8뿐)
print(sum(last[N-1])%1000000000) # 나머지