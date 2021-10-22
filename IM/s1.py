T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pattern = list(map(int, input().split()))

    result = 0
    LED = [0] * N

    for i in range(N):
        if LED[i] != pattern[i]:
            result +=1
            for j in range(1, N//(i+1) + 1):
                LED[(i+1) * j - 1] = 1 - LED[(i+1) * j - 1]
    print('#{} {}'.format(tc, result))