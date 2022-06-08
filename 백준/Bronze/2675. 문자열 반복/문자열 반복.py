T = int(input())
for tc in range(1, T+1):
    R, S = input().split()
    for s in S:
        for _ in range(int(R)):
            print(s, end="")
    print()