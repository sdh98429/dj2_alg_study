# ! 분산처리, 1의 자리수 배열로
T = int(input())

for tc in range(1, T+1):
    a, b = list(map(int, input().split()))
    a %= 10
    new = a
    hist = [new]
    for _ in range(b-1):
        new *= a
        new %= 10
        
        if new != hist[0]:
            hist.append(new)
        else:
            break
        
    print(hist[(b-1)%len(hist)] if hist[(b-1)%len(hist)] else 10) # 0이면 10으로 변환