T = int(input())

for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    print(min(L), max(L))