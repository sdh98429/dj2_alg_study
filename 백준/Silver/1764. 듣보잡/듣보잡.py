import sys

N, M = map(int, sys.stdin.readline().split())

Hear = set(sys.stdin.readline().rstrip() for _ in range(N))
See = set(sys.stdin.readline().rstrip() for _ in range(M))

HearSee = Hear & See
HearSeeList = list(HearSee)
print(len(HearSeeList))
print(*sorted(HearSeeList), sep='\n')