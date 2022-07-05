H, M = map(int, input().split())
T = (60 * H + M - 45)% (60 * 24)
print(T//60, T%60)