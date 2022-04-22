# 평균은 넘겠지

C = int(input())

for tc in range(1, C+1):
    L = list(map(int, input().split()))
    avg = sum(L[1:])/L[0]
    n = 0
    for l in L[1:]:
        if l > avg:
            n += 1
    print('{0:.3f}%'.format(n/L[0]*100))
