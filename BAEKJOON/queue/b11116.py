# queue 교통량, left, right 각각 케이스 하나로 줄이려 삽질
T = int(input())

for tc in range(1, T+1):
    m = int(input())
    l_box = list(map(int, input().split()))
    r_box = list(map(int, input().split()))
    front = 0
    left = []
    right = []
    ans = 0
    for _ in range(m):
        if l_box[front] + 1000 in r_box:
           ans += 1
        front += 1
    print(ans//2)
